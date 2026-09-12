import { createContext, useContext, useEffect, useMemo, useState } from "react";
import { api, getToken, setToken, type User } from "../api/client";

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
