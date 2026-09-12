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
