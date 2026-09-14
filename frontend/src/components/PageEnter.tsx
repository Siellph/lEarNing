import { Outlet, useLocation } from "react-router-dom";

/** Re-runs enter motion on route change without remounting the app shell. */
export function PageEnter() {
  const { pathname } = useLocation();
  return (
    <div key={pathname} className="motion-enter min-w-0">
      <Outlet />
    </div>
  );
}
