import { createContext, useContext, useEffect, useMemo, useState } from "react";
import { api, getToken, getTokenExpiresAt, setToken, type User } from "../api/client";

/** Refresh when less than 2 hours remain on the access token. */
const REFRESH_WITHIN_MS = 2 * 60 * 60 * 1000;
/** Periodic check while the tab is open. */
const REFRESH_CHECK_INTERVAL_MS = 15 * 60 * 1000;

type AuthState = {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<User>;
  register: (
    name: string,
    email: string,
    password: string,
    acceptedTerms: boolean,
  ) => Promise<{ user: User | null; message?: string; email?: string }>;
  logout: () => void;
  refresh: () => Promise<void>;
};

const Ctx = createContext<AuthState | null>(null);

let refreshInflight: Promise<boolean> | null = null;

/** Extend the access JWT without clearing session or redirecting on failure. */
async function silentRefreshAccessToken(): Promise<boolean> {
  const token = getToken();
  if (!token) return false;
  const expiresAt = getTokenExpiresAt(token);
  if (expiresAt == null) return false;
  const remaining = expiresAt - Date.now();
  if (remaining > REFRESH_WITHIN_MS) return true;
  if (remaining <= 0) return false;

  if (refreshInflight) return refreshInflight;

  refreshInflight = (async () => {
    try {
      const res = await fetch("/api/auth/refresh", {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
      });
      if (!res.ok) return false;
      const data = (await res.json()) as { access_token?: string };
      if (!data.access_token) return false;
      setToken(data.access_token);
      return true;
    } catch {
      return false;
    } finally {
      refreshInflight = null;
    }
  })();

  return refreshInflight;
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  const refresh = async () => {
    if (!getToken()) {
      setUser(null);
      setLoading(false);
      return;
    }
    try {
      await silentRefreshAccessToken();
      const me = await api<User>("/auth/me");
      setUser(me);
    } catch {
      setToken(null);
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    refresh();
  }, []);

  useEffect(() => {
    if (!user) return;

    const maybeRefresh = () => {
      void silentRefreshAccessToken();
    };

    maybeRefresh();
    const id = window.setInterval(maybeRefresh, REFRESH_CHECK_INTERVAL_MS);

    const onFocus = () => maybeRefresh();
    const onVisibility = () => {
      if (document.visibilityState === "visible") maybeRefresh();
    };

    window.addEventListener("focus", onFocus);
    document.addEventListener("visibilitychange", onVisibility);

    return () => {
      window.clearInterval(id);
      window.removeEventListener("focus", onFocus);
      document.removeEventListener("visibilitychange", onVisibility);
    };
  }, [user]);

  const login = async (email: string, password: string) => {
    const data = await api<{ access_token: string }>("/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
    setToken(data.access_token);
    const me = await api<User>("/auth/me");
    setUser(me);
    return me;
  };

  const register = async (name: string, email: string, password: string, acceptedTerms: boolean) => {
    const data = await api<{ access_token?: string; message?: string; email?: string }>("/auth/register", {
      method: "POST",
      body: JSON.stringify({ name, email, password, accepted_terms: acceptedTerms }),
    });
    if (data.access_token) {
      setToken(data.access_token);
      const me = await api<User>("/auth/me");
      setUser(me);
      return { user: me };
    }
    return { user: null, message: data.message, email: data.email };
  };

  const logout = () => {
    setToken(null);
    setUser(null);
  };

  const value = useMemo(
    () => ({ user, loading, login, register, logout, refresh }),
    [user, loading],
  );

  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}

export function useAuth() {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error("useAuth outside provider");
  return ctx;
}
