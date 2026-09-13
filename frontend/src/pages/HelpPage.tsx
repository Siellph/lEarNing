import { Link } from "react-router-dom";
import { KIND_LABELS } from "../lib/kindLabels";

type Guide = {
  kind: keyof typeof KIND_LABELS;
  title: string;
  what: string;
  how: string;
  example: { prompt: string; do: string; answer: string };
};

const GUIDES: Guide[] = [
  {
    kind: "fill_blank",
    title: KIND_LABELS.fill_blank,
    what: "В предложении есть пропуск ___ — нужно вставить слово или форму.",
    how: "Пишите только то, что входит в пропуск. Если пропусков несколько, заполните каждый по порядку.",
    example: {
      prompt: "He ___ a teacher. (be)",
      do: "В пропуск — форма to be для he.",
      answer: "is",
    },
  },
  {
    kind: "transform",
    title: KIND_LABELS.transform,
    what: "Нужно изменить предложение: время, число, отрицание, вопрос и т.п.",
    how: "Перепишите предложение целиком в нужной форме — не только глагол.",
    example: {
      prompt: "Отрицание: We are ready.",
      do: "Сделайте отрицание Present Simple с be.",
      answer: "We are not ready. / We aren't ready.",
    },
  },
  {
    kind: "error_correction",
    title: KIND_LABELS.error_correction,
    what: "В предложении есть ошибка. Нужно дать правильный вариант.",
    how: "Перепишите всё предложение правильно. Недостаточно исправить одно слово в уме — введите полный правильный текст.",
    example: {
      prompt: "I have seen him yesterday.",
      do: "Yesterday требует Past Simple, не Present Perfect.",
      answer: "I saw him yesterday.",
    },
  },
  {
    kind: "order",
    title: KIND_LABELS.order,
    what: "Даны слова вперемешку — соберите нормальное английское предложение.",
    how: "Напишите фразу целиком с заглавной буквы и точкой, если так принято в ответе.",
    example: {
      prompt: "from / are / they / Spain",
      do: "Порядок: подлежащее → are → дополнение.",
      answer: "They are from Spain.",
    },
  },
  {
    kind: "multiple_choice",
    title: KIND_LABELS.multiple_choice,
    what: "Несколько вариантов — выберите один верный.",
    how: "Нажмите на подходящий вариант, затем «Проверить».",
    example: {
      prompt: "___ she a doctor?",
      do: "Вопрос с she → Is.",
      answer: "Is",
    },
  },
  {
    kind: "match",
    title: KIND_LABELS.match,
    what: "Слева слоты, справа формы — нужно сопоставить пары.",
    how: "Нажмите чип, затем пустой слот (или наоборот). Чтобы вернуть чип — нажмите его в слоте. «Проверить» доступна, когда все слоты заполнены.",
    example: {
      prompt: "yesterday · since 2020 · already",
      do: "Маркеры времени → Past / Perfect.",
      answer: "yesterday→Past; since 2020→Perfect; already→Perfect",
    },
  },
];

export function HelpPage() {
  return (
    <div className="mx-auto grid max-w-3xl gap-6 pb-8">
      <div>
        <p className="text-sm uppercase tracking-[0.16em] text-terra">Справка</p>
        <h1 className="font-display mt-1 text-4xl">Как решать задания</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">
          Краткие пояснения и примеры к типам упражнений в практике, тестах и экзаменах. Наведите на
          английское слово в задании — часто появится перевод.
        </p>
      </div>

      <div className="grid gap-4">
        {GUIDES.map((g) => (
          <section key={g.kind} className="quiz-card overflow-hidden">
            <header className="quiz-card-head">
              <span className="quiz-kind">{g.title}</span>
            </header>
            <div className="grid gap-3 p-5 sm:p-6">
              <p className="leading-relaxed">{g.what}</p>
              <p className="text-sm leading-relaxed text-ink-soft">{g.how}</p>
              <div className="rounded-2xl border border-line/80 bg-paper/80 p-4">
                <p className="text-xs font-semibold uppercase tracking-wide text-ink-soft">Пример</p>
                <p className="mt-2 font-medium leading-relaxed">{g.example.prompt}</p>
                <p className="mt-1 text-sm text-ink-soft">{g.example.do}</p>
                <p className="mt-3 text-sm">
                  <span className="font-semibold text-sage">Ответ: </span>
                  {g.example.answer}
                </p>
              </div>
            </div>
          </section>
        ))}
      </div>

      <p className="text-sm text-ink-soft">
        Вернуться к учёбе:{" "}
        <Link to="/app/grammar" className="font-semibold text-terra">
          Грамматика
        </Link>
      </p>
    </div>
  );
}
