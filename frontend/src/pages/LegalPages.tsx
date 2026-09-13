import { Link } from "react-router-dom";
import { BrandMark } from "../components/BrandMark";

function LegalShell({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="surface-grid min-h-screen px-4 py-10">
      <div className="mx-auto w-full max-w-3xl">
        <Link to="/" className="inline-block">
          <BrandMark size="md" />
          <p className="mt-1 text-sm text-ink-soft">учим EN</p>
        </Link>
        <article className="card mt-6 p-6 sm:p-8">
          <p className="text-sm text-ink-soft">Обновлено 13 сентября 2026</p>
          <h1 className="mt-2 font-display text-3xl sm:text-4xl">{title}</h1>
          <div className="mt-6 grid gap-5 text-[1.05rem] leading-7 text-ink-soft">{children}</div>
        </article>
        <p className="mt-6 flex flex-wrap gap-4 text-sm text-ink-soft">
          <Link to="/about" className="text-terra">
            О проекте
          </Link>
          <Link to="/terms" className="text-terra">
            Пользовательское соглашение
          </Link>
          <Link to="/privacy" className="text-terra">
            Политика конфиденциальности
          </Link>
          <Link to="/register" className="text-terra">
            Регистрация
          </Link>
        </p>
      </div>
    </div>
  );
}

export function TermsPage() {
  return (
    <LegalShell title="Пользовательское соглашение">
      <p>
        Это типовые положения учебного проекта <strong className="text-ink">lEarNing</strong> («сервис»).
        Сервис помогает изучать английский язык: грамматика, словарь, звуки, практика и экзамены. Документ
        не является юридической консультацией и не заменяет договор с профессиональной образовательной
        организацией.
      </p>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">1. Услуга</h2>
        <p>
          Мы предоставляем доступ к учебным материалам и личному кабинету. Сервис носит образовательный и
          ознакомительный характер. Мы не гарантируем сдачу внешних экзаменов (IELTS, TOEFL, Cambridge и
          др.), определённый уровень языка или конкретный результат обучения.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">2. Аккаунт</h2>
        <p>
          Для регистрации нужны имя, адрес электронной почты и пароль. Вы отвечаете за сохранность пароля и
          за действия в своём аккаунте. Один аккаунт — для личного использования. Если сервис запрашивает
          подтверждение email, вход возможен после подтверждения.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">3. Правила использования</h2>
        <p>
          Нельзя взламывать сервис, мешать его работе, выдавать себя за другого человека, распространять
          вредоносный код, копировать учебный контент для коммерции или массовой перепечатки, оскорблять
          других пользователей или использовать сервис незаконно. Мы можем ограничить или отключить
          аккаунт при нарушениях.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">4. Интеллектуальная собственность</h2>
        <p>
          Тексты уроков, упражнения, структура курса и оформление принадлежат проекту lEarNing или
          используются на законных основаниях. Карта тем опирается на открытые учебные структуры (CEFR и
          др.), но сам контент сервиса копировать целиком нельзя. Личный прогресс остаётся вашим.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">5. Ограничение ответственности</h2>
        <p>
          Сервис предоставляется «как есть». Возможны ошибки в материалах, перерывы в работе и потеря
          несохранённых данных. Мы не отвечаем за косвенный ущерб, упущенную выгоду или решения, принятые
          только на основе курса.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">6. Изменения и контакты</h2>
        <p>
          Мы можем обновлять сервис и это соглашение. Актуальная версия публикуется на этой странице.
          Вопросы: напишите администратору проекта или используйте контакт, указанный в интерфейсе сервиса.
        </p>
      </section>
    </LegalShell>
  );
}

export function PrivacyPage() {
  return (
    <LegalShell title="Политика конфиденциальности">
      <p>
        Учебный проект <strong className="text-ink">lEarNing</strong> обрабатывает минимум данных, чтобы
        создать аккаунт и сохранить прогресс. Ниже — типовые положения: что собираем, зачем и какие у вас
        есть права.
      </p>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">1. Какие данные собираем</h2>
        <p>
          При регистрации — имя, email и пароль (хранится в виде хеша). В процессе учёбы — прогресс по
          модулям, попытки упражнений, тестов и экзаменов, словарь, опыт (XP) и серия дней. Если включена
          проверка почты, сохраняем одноразовые токены подтверждения.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">2. Зачем это нужно</h2>
        <p>
          Email и имя — чтобы войти в кабинет и обращаться к вам. Пароль — чтобы защитить аккаунт. Прогресс
          — чтобы продолжить обучение с того места, где остановились. Письмо с подтверждением — чтобы
          убедиться, что почта принадлежит вам.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">3. Cookie, local storage и JWT</h2>
        <p>
          Сервис не ставит HTTP-cookie и не подключает рекламу, пиксели или аналитику вроде Google
          Analytics. После входа токен доступа (JWT) хранится в local storage браузера
          (<code className="text-ink">lumina_token</code>) — без него кабинет не работает. Если вы
          приняли дополнительные настройки, там же сохраняются акцент и темп озвучки
          (<code className="text-ink">lumina_accent</code>,{" "}
          <code className="text-ink">lumina_speech_rate</code>). Выбор в баннере внизу страницы
          записывается в <code className="text-ink">learning_cookie_consent</code>. При отказе
          остаются только необходимые данные входа; настройки речи действуют до закрытия вкладки и не
          записываются.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">4. Передача и продажа</h2>
        <p>
          Мы не продаём персональные данные. Доступ к ним есть у администраторов сервиса и, при размещении
          на хостинге, у инфраструктуры (сервер, почта), без которой сервис не работает.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">5. Ваши права и удаление</h2>
        <p>
          Вы можете изменить имя и пароль в профиле. Самостоятельного удаления аккаунта в интерфейсе пока
          нет: напишите администратору, и мы удалим или отключим учётную запись вместе с учебным прогрессом,
          если это технически возможно.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">6. Срок хранения</h2>
        <p>
          Данные аккаунта хранятся, пока он активен. Токены подтверждения почты живут недолго и удаляются
          после использования или истечения срока. Отключённые аккаунты могут оставаться в базе, пока их не
          удалит администратор.
        </p>
      </section>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl text-ink">7. Контакты</h2>
        <p>
          Вопросы по персональным данным направляйте администратору lEarNing. Актуальная версия политики —
          на этой странице; дата обновления указана выше.
        </p>
      </section>
    </LegalShell>
  );
}
