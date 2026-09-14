import { useEffect } from "react";
import { Link } from "react-router-dom";
import { BrandMark } from "../components/BrandMark";

export function AboutPage() {
  useEffect(() => {
    const prev = document.title;
    document.title = "О проекте — lEarNinG";
    return () => {
      document.title = prev;
    };
  }, []);

  return (
    <div className="surface-grid min-h-screen px-4 py-10">
      <div className="mx-auto w-full max-w-3xl">
        <Link to="/" className="inline-block">
          <BrandMark size="md" />
          <p className="mt-1 text-sm text-ink-soft">учим ENG</p>
        </Link>

        <article className="mt-8">
          <p className="text-sm font-semibold uppercase tracking-[0.2em] text-terra">О проекте</p>
          <h1 className="mt-3 font-display text-3xl text-ink sm:text-4xl">lEarNinG — учим ENG</h1>
          <p className="mt-5 text-[1.05rem] leading-8 text-ink-soft">
            Название читается как <strong className="text-ink">learning</strong> и одновременно как{" "}
            <strong className="text-ink">учим ENG</strong>: небольшой учебный сервис для тех, кто хочет
            спокойно разобраться в английском — без рекламы курса «за три недели» и без имитации крупной
            школы.
          </p>

          <section className="mt-10 grid gap-3">
            <h2 className="font-display text-2xl text-ink">Для кого</h2>
            <p className="text-[1.05rem] leading-8 text-ink-soft">
              Для самостоятельных учеников: от нуля до уверенного C2, если уже есть база или хочется
              закрыть пробелы. Подойдёт школьникам, студентам и взрослым, которым удобнее учить теорию на
              русском, а примеры — на английском.
            </p>
          </section>

          <section className="mt-10 grid gap-3">
            <h2 className="font-display text-2xl text-ink">Что внутри</h2>
            <p className="text-[1.05rem] leading-8 text-ink-soft">
              Грамматика по уровням CEFR от A1 до C2: уроки, практика после темы, тесты модулей и
              экзамены уровня. Рядом — словарь по темам, звуки и чтение (IPA, правила), а также глаголы,
              идиомы и типичные исключения — чтобы закреплять не только правила, но и живые куски языка.
            </p>
          </section>

          <section className="mt-10 grid gap-3">
            <h2 className="font-display text-2xl text-ink">Как устроены материалы</h2>
            <p className="text-[1.05rem] leading-8 text-ink-soft">
              Пояснения написаны по-русски, примеры и задания — на английском. Смысл простой: понять
              правило на родном языке и сразу увидеть, как оно звучит в настоящей фразе.
            </p>
          </section>

          <section className="mt-10 grid gap-3">
            <h2 className="font-display text-2xl text-ink">Свободный учебный проект</h2>
            <p className="text-[1.05rem] leading-8 text-ink-soft">
              lEarNinG — образовательный проект, а не коммерческая платформа с обещаниями дипломов и
              «гарантированного уровня». Материалы открыты для обучения; аккаунт нужен, чтобы сохранить
              прогресс. Это помощник для практики, а не единственный или окончательный источник по
              языку: для экзаменов и официальных требований лучше сверяться с учебниками и
              специалистами.
            </p>
          </section>

          <div className="mt-12 flex flex-wrap gap-3">
            <Link to="/register" className="btn btn-primary">
              Создать аккаунт
            </Link>
            <Link to="/login" className="btn btn-ghost">
              Войти
            </Link>
          </div>
        </article>

        <p className="mt-10 flex flex-wrap gap-4 text-sm text-ink-soft">
          <Link to="/terms" className="text-terra hover:underline">
            Пользовательское соглашение
          </Link>
          <Link to="/privacy" className="text-terra hover:underline">
            Политика конфиденциальности
          </Link>
          <Link to="/" className="hover:text-terra">
            На главную
          </Link>
        </p>
      </div>
    </div>
  );
}
