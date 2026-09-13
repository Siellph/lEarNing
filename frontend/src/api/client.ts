const API = "/api";

export class ApiError extends Error {
  status: number;
  constructor(status: number, message: string) {
    super(message);
    this.status = status;
  }
}

export function getToken() {
  return localStorage.getItem("lumina_token");
}

export function setToken(token: string | null) {
  if (token) localStorage.setItem("lumina_token", token);
  else localStorage.removeItem("lumina_token");
}

/** Decode JWT payload without verifying (client-side expiry checks only). */
export function getTokenExpiresAt(token: string | null = getToken()): number | null {
  if (!token) return null;
  try {
    const part = token.split(".")[1];
    if (!part) return null;
    const b64 = part.replace(/-/g, "+").replace(/_/g, "/");
    const padded = b64.padEnd(b64.length + ((4 - (b64.length % 4)) % 4), "=");
    const payload = JSON.parse(atob(padded)) as { exp?: number };
    return typeof payload.exp === "number" ? payload.exp * 1000 : null;
  } catch {
    return null;
  }
}

export async function api<T>(path: string, options: RequestInit = {}): Promise<T> {
  const headers = new Headers(options.headers);
  if (!headers.has("Content-Type") && options.body) headers.set("Content-Type", "application/json");
  const token = getToken();
  if (token) headers.set("Authorization", `Bearer ${token}`);

  const res = await fetch(`${API}${path}`, { ...options, headers });
  if (res.status === 401) {
    setToken(null);
    if (
      !path.startsWith("/auth/login") &&
      !path.startsWith("/auth/register") &&
      !path.startsWith("/auth/verify") &&
      !path.startsWith("/auth/resend-verification")
    ) {
      window.location.href = "/login";
    }
  }
  if (!res.ok) {
    let detail = "Не удалось выполнить запрос";
    try {
      const data = await res.json();
      detail = typeof data.detail === "string" ? data.detail : detail;
    } catch {
      /* ignore */
    }
    throw new ApiError(res.status, detail);
  }
  if (res.status === 204) return undefined as T;
  return res.json();
}

export type User = {
  id: number;
  email: string;
  name: string;
  role: string;
  email_verified: boolean;
  xp: number;
  streak: number;
  last_activity: string | null;
  created_at: string;
};
