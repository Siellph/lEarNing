import { LoaderCircle, Search, X } from "lucide-react";
import { useEffect, useId, useRef, useState, type KeyboardEvent, type RefObject } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../api/client";
import { clearAppScroll, scrollAppToTop } from "../lib/scrollRestore";

export type SearchHit = {
  section: string;
  title: string;
  subtitle?: string;
  href: string;
};

type SearchResponse = {
  query: string;
  results: SearchHit[];
};

const DEBOUNCE_MS = 250;

function goSearchHit(navigate: ReturnType<typeof useNavigate>, href: string) {
  try {
    const url = new URL(href, window.location.origin);
    clearAppScroll(url.pathname);
  } catch {
    /* ignore */
  }
  scrollAppToTop();
  navigate(href);
}

function useDebouncedValue<T>(value: T, delay: number) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const id = window.setTimeout(() => setDebounced(value), delay);
    return () => window.clearTimeout(id);
  }, [value, delay]);
  return debounced;
}

function useLiveSearch(query: string, enabled: boolean) {
  const debounced = useDebouncedValue(query, DEBOUNCE_MS);
  const [results, setResults] = useState<SearchHit[]>([]);
  const [loading, setLoading] = useState(false);
  const requestId = useRef(0);

  useEffect(() => {
    if (!enabled) return;
    const q = debounced.trim();
    if (q.length < 2) {
      setResults([]);
      setLoading(false);
      return;
    }
    const current = ++requestId.current;
    setLoading(true);
    api<SearchResponse>(`/search?q=${encodeURIComponent(q)}`)
      .then((data) => {
        if (current !== requestId.current) return;
        setResults(data.results);
      })
      .catch(() => {
        if (current !== requestId.current) return;
        setResults([]);
      })
      .finally(() => {
        if (current === requestId.current) setLoading(false);
      });
  }, [debounced, enabled]);

  return { results, loading };
}

function ResultList({
  results,
  loading,
  query,
  activeIndex,
  onHover,
  onSelect,
  listId,
}: {
  results: SearchHit[];
  loading: boolean;
  query: string;
  activeIndex: number;
  onHover: (index: number) => void;
  onSelect: (hit: SearchHit) => void;
  listId: string;
}) {
  if (query.trim().length < 2) {
    return <p className="px-3 py-4 text-sm text-ink-soft">Введите хотя бы 2 символа</p>;
  }
  if (loading) {
    return (
      <p className="flex items-center gap-2 px-3 py-4 text-sm text-ink-soft">
        <LoaderCircle size={16} className="animate-spin" />
        Ищем…
      </p>
    );
  }
  if (!results.length) {
    return <p className="px-3 py-4 text-sm text-ink-soft">Ничего не найдено</p>;
  }

  return (
    <ul id={listId} role="listbox" className="max-h-[min(22rem,55vh)] overflow-y-auto py-1">
      {results.map((hit, index) => {
        const active = index === activeIndex;
        return (
          <li key={`${hit.href}|${hit.subtitle ?? ""}|${hit.title}`} role="option" aria-selected={active}>
            <button
              type="button"
              className={`flex w-full flex-col gap-0.5 px-3 py-2.5 text-left transition-colors ${
                active ? "bg-sage-soft/70" : "hover:bg-paper-2/80"
              }`}
              onMouseEnter={() => onHover(index)}
              onClick={() => onSelect(hit)}
            >
              <span className="text-[0.7rem] font-semibold uppercase tracking-[0.12em] text-terra">
                {hit.section}
              </span>
              <span className="text-sm font-semibold text-ink">{hit.title}</span>
              {hit.subtitle ? <span className="text-xs text-ink-soft">{hit.subtitle}</span> : null}
            </button>
          </li>
        );
      })}
    </ul>
  );
}

function SearchField({
  query,
  setQuery,
  onKeyDown,
  onFocus,
  listId,
  inputRef,
  expanded,
}: {
  query: string;
  setQuery: (value: string) => void;
  onKeyDown: (event: KeyboardEvent<HTMLInputElement>) => void;
  onFocus?: () => void;
  listId: string;
  inputRef: RefObject<HTMLInputElement | null>;
  expanded: boolean;
}) {
  return (
    <div className="search-field-wrap">
      <Search size={16} className="search-field-icon" aria-hidden />
      <input
        ref={inputRef}
        className="search-field"
        type="search"
        value={query}
        placeholder="Поиск по курсу…"
        aria-autocomplete="list"
        aria-controls={listId}
        aria-expanded={expanded}
        autoComplete="off"
        onFocus={onFocus}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={onKeyDown}
      />
      {query ? (
        <button
          type="button"
          className="search-field-clear inline-flex size-7 items-center justify-center rounded-full text-ink-soft hover:bg-paper-2 hover:text-ink"
          aria-label="Очистить"
          onClick={() => {
            setQuery("");
            inputRef.current?.focus();
          }}
        >
          <X size={14} />
        </button>
      ) : null}
    </div>
  );
}

function DesktopSearch() {
  const navigate = useNavigate();
  const wrapRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const listId = useId();
  const [query, setQuery] = useState("");
  const [open, setOpen] = useState(false);
  const [activeIndex, setActiveIndex] = useState(0);
  const { results, loading } = useLiveSearch(query, open);
  const showPanel = open && query.trim().length >= 1;

  useEffect(() => {
    setActiveIndex(0);
  }, [results]);

  useEffect(() => {
    if (!open) return;
    const onPointer = (event: MouseEvent) => {
      if (!wrapRef.current?.contains(event.target as Node)) {
        setOpen(false);
      }
    };
    document.addEventListener("mousedown", onPointer);
    return () => document.removeEventListener("mousedown", onPointer);
  }, [open]);

  const selectHit = (hit: SearchHit) => {
    setOpen(false);
    setQuery("");
    goSearchHit(navigate, hit.href);
  };

  const onKeyDown = (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Escape") {
      event.preventDefault();
      setOpen(false);
      inputRef.current?.blur();
      return;
    }
    if (!results.length) return;
    if (event.key === "ArrowDown") {
      event.preventDefault();
      setOpen(true);
      setActiveIndex((i) => (i + 1) % results.length);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      setActiveIndex((i) => (i - 1 + results.length) % results.length);
    } else if (event.key === "Enter") {
      event.preventDefault();
      const hit = results[activeIndex];
      if (hit) selectHit(hit);
    }
  };

  return (
    <div ref={wrapRef} className="relative hidden w-[min(18rem,28vw)] min-[721px]:block">
      <SearchField
        query={query}
        setQuery={(value) => {
          setQuery(value);
          setOpen(true);
        }}
        onFocus={() => setOpen(true)}
        onKeyDown={onKeyDown}
        listId={listId}
        inputRef={inputRef}
        expanded={showPanel}
      />
      {showPanel ? (
        <div
          className="absolute right-0 top-[calc(100%+0.4rem)] z-50 w-[min(24rem,calc(100vw-2rem))] overflow-hidden rounded-2xl border border-line/80 bg-card shadow-[0_18px_40px_-20px_rgba(18,32,51,0.35)]"
          role="listbox"
          aria-label="Результаты поиска"
        >
          <ResultList
            results={results}
            loading={loading}
            query={query}
            activeIndex={activeIndex}
            onHover={setActiveIndex}
            onSelect={selectHit}
            listId={listId}
          />
        </div>
      ) : null}
    </div>
  );
}

function MobileSearch() {
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);
  const openBtnRef = useRef<HTMLButtonElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const panelRef = useRef<HTMLDivElement>(null);
  const listId = useId();
  const titleId = useId();
  const [query, setQuery] = useState("");
  const [activeIndex, setActiveIndex] = useState(0);
  const { results, loading } = useLiveSearch(query, open);

  useEffect(() => {
    if (!open) return;
    setQuery("");
    setActiveIndex(0);
    const id = window.requestAnimationFrame(() => inputRef.current?.focus());
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      window.cancelAnimationFrame(id);
      document.body.style.overflow = prev;
    };
  }, [open]);

  useEffect(() => {
    setActiveIndex(0);
  }, [results]);

  useEffect(() => {
    if (!open) return;
    const onKey = (event: globalThis.KeyboardEvent) => {
      if (event.key !== "Tab" || !panelRef.current) return;
      const focusable = panelRef.current.querySelectorAll<HTMLElement>(
        'a[href], button:not([disabled]), input:not([disabled]), [tabindex]:not([tabindex="-1"])',
      );
      if (!focusable.length) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [open]);

  const close = () => {
    setOpen(false);
    window.requestAnimationFrame(() => openBtnRef.current?.focus());
  };

  const selectHit = (hit: SearchHit) => {
    close();
    goSearchHit(navigate, hit.href);
  };

  const onKeyDown = (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Escape") {
      event.preventDefault();
      close();
      return;
    }
    if (!results.length) return;
    if (event.key === "ArrowDown") {
      event.preventDefault();
      setActiveIndex((i) => (i + 1) % results.length);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      setActiveIndex((i) => (i - 1 + results.length) % results.length);
    } else if (event.key === "Enter") {
      event.preventDefault();
      const hit = results[activeIndex];
      if (hit) selectHit(hit);
    }
  };

  return (
    <>
      <button
        ref={openBtnRef}
        type="button"
        className="inline-flex size-10 items-center justify-center rounded-xl border border-line/80 bg-card text-ink shadow-sm hover:bg-paper-2 max-[720px]:inline-flex min-[721px]:hidden"
        aria-label="Открыть поиск"
        aria-expanded={open}
        onClick={() => setOpen(true)}
      >
        <Search size={18} />
      </button>

      {open ? (
        <div className="fixed inset-0 z-[60] flex items-start justify-center bg-ink/40 p-3 pt-[max(0.75rem,env(safe-area-inset-top))]">
          <button type="button" className="absolute inset-0 cursor-default" aria-label="Закрыть поиск" onClick={close} />
          <div
            ref={panelRef}
            role="dialog"
            aria-modal="true"
            aria-labelledby={titleId}
            className="relative z-[61] mt-2 flex w-full max-w-lg flex-col overflow-hidden rounded-2xl border border-line/80 bg-card shadow-[0_20px_50px_-24px_rgba(18,32,51,0.45)]"
          >
            <div className="flex items-center justify-between gap-2 border-b border-line/70 px-4 py-3">
              <p id={titleId} className="font-display text-lg text-ink">
                Поиск
              </p>
              <button
                type="button"
                className="inline-flex size-10 items-center justify-center rounded-xl border border-line/80 bg-paper text-ink hover:bg-paper-2"
                aria-label="Закрыть"
                onClick={close}
              >
                <X size={18} />
              </button>
            </div>
            <div className="border-b border-line/60 px-3 py-3">
              <SearchField
                query={query}
                setQuery={setQuery}
                onKeyDown={onKeyDown}
                listId={listId}
                inputRef={inputRef}
                expanded={query.trim().length >= 2}
              />
            </div>
            <ResultList
              results={results}
              loading={loading}
              query={query}
              activeIndex={activeIndex}
              onHover={setActiveIndex}
              onSelect={selectHit}
              listId={listId}
            />
          </div>
        </div>
      ) : null}
    </>
  );
}

export function GlobalSearch() {
  return (
    <>
      <DesktopSearch />
      <MobileSearch />
    </>
  );
}
