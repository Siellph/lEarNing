type BrandSize = "sm" | "md" | "lg" | "hero";

const sizes: Record<BrandSize, string> = {
  sm: "text-xl",
  md: "text-2xl",
  lg: "text-3xl",
  hero: "text-6xl leading-[0.95] sm:text-8xl",
};

const accents: Record<BrandSize, string> = {
  sm: "text-terra",
  md: "text-terra",
  lg: "text-terra underline decoration-terra/35 decoration-2 underline-offset-[0.12em]",
  hero: "text-terra underline decoration-terra/40 decoration-[3px] underline-offset-[0.14em]",
};

/** Brand: lEarNinG — capitals E·N·G spell ENG. */
export function BrandMark({ size = "md", className = "" }: { size?: BrandSize; className?: string }) {
  const accent = accents[size];
  return (
    <span className={`font-display tracking-tight ${sizes[size]} ${className}`} aria-label="lEarNinG">
      l<span className={accent}>E</span>ar<span className={accent}>N</span>in<span className={accent}>G</span>
    </span>
  );
}
