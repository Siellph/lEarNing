import { ArrowRight, BookOpenCheck, PenLine, Trophy, Volume2 } from "lucide-react";
import { Link } from "react-router-dom";
import { BrandMark } from "../components/BrandMark";
import { DonationBanner } from "../components/DonationBanner";

export function Landing() {
  return (
    <div className="surface-grid flex min-h-dvh flex-col">
      <DonationBanner />
      <header className="mx-auto flex w-full max-w-6xl shrink-0 items-center justify-between px-5 py-5">
        <div>
          <BrandMark size="md" />
          <p className="text-xs text-ink-soft">учим ENG</p>
        </div>
        <div className="flex gap-2">
          <Link to="/login" className="btn btn-ghost">
            Войти
          </Link>
          <Link to="/register" className="btn btn-primary">
            Начать
          </Link>
        </div>
      </header>
      <section className="motion-enter mx-auto grid w-full max-w-6xl flex-1 items-center gap-10 px-5 py-[clamp(1.5rem,4vh,2.5rem)] lg:grid-cols-2">
        <div>
          <p className="mb-3 text-sm font-semibold uppercase tracking-[0.2em] text-terra">CEFR A1–C2</p>
          <h1>
            <BrandMark size="hero" />
          </h1>
          <p className="mt-5 font-display text-2xl text-ink-soft sm:text-3xl">lEarNinG — учим ENG</p>
          <p className="mt-4 max-w-xl text-lg leading-8 text-ink-soft">
            Английская грамматика целиком — блоками, с практикой и экзаменами. Теория на русском,
            примеры на английском, закрепление сразу после урока.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Link to="/register" className="btn btn-primary">
              Создать аккаунт <ArrowRight size={18} />
            </Link>
            <Link to="/login" className="btn btn-ghost">
              Войти
            </Link>
          </div>
        </div>
        <div className="card p-6 sm:p-8">
          <p className="font-display text-2xl">Как устроен курс</p>
          <ul className="mt-6 grid gap-5">
            {[
              { icon: BookOpenCheck, title: "76 грамматических блоков", text: "От to be до информационного порядка слов и регистра C2." },
              { icon: PenLine, title: "Практика после каждой темы", text: "Выбор, пропуски, преобразования и исправление ошибок." },
              { icon: Trophy, title: "Тесты модуля и экзамены уровня", text: "Порог 70% на тест, 75% на экзамен. Прогресс и серия дней." },
              { icon: Volume2, title: "Озвучка и транскрипция", text: "Слушайте слова и фразы, разбирайте IPA, правила чтения и связную речь." },
            ].map((item) => (
              <li key={item.title} className="flex gap-4">
                <div className="grid h-11 w-11 shrink-0 place-items-center rounded-2xl bg-paper-2 text-terra">
                  <item.icon size={20} />
                </div>
                <div>
                  <p className="font-semibold">{item.title}</p>
                  <p className="text-sm leading-6 text-ink-soft">{item.text}</p>
                </div>
              </li>
            ))}
          </ul>
        </div>
      </section>
      <footer className="mx-auto flex w-full max-w-6xl shrink-0 flex-wrap items-center gap-x-5 gap-y-2 px-5 py-8 text-sm text-ink-soft">
        <span>© 2026 lEarNinG</span>
        <Link to="/about" className="hover:text-terra">
          О проекте
        </Link>
        <Link to="/terms" className="hover:text-terra">
          Пользовательское соглашение
        </Link>
        <Link to="/privacy" className="hover:text-terra">
          Политика конфиденциальности
        </Link>
      </footer>
    </div>
  );
}
