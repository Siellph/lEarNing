# lEarNing

lEarNing — учим EN (learning EN). Веб-сервис для изучения английского: грамматика по блокам CEFR A1–C2, практика, тесты модулей, экзамены уровней, тематический словарь, кабинет ученика и админ-панель.

Теория написана самостоятельно на русском. Тематическая карта опирается на открытые учебные структуры **CEFR / Cambridge English**, **British Council LearnEnglish**, **Oxford Practice Grammar** и **English Grammar in Use** (карта тем, не текст учебников).

## Стек

- Python 3.12, FastAPI, SQLAlchemy, PostgreSQL 16
- React 19, TypeScript, Vite, Tailwind CSS 4
- Docker Compose

## Запуск

```bash
docker compose up --build
```

Откройте [http://localhost:3000](http://localhost:3000).

Первый администратор создаётся при сиде из `ADMIN_EMAIL` и `ADMIN_PASSWORD` в `.env` (см. `.env.example`), не с сайта. Если переменные не заданы, админа нет. Уже существующего пользователя можно повысить вручную: `UPDATE users SET role = 'admin' WHERE email = 'you@example.com';` (в Docker: `docker compose exec postgres psql -U lumina -d lumina`).

API: [http://localhost:8000/docs](http://localhost:8000/docs)

Повторный запуск не перезаписывает учебный контент: сидер идемпотентен. На пустой БД заливает грамматику, экзамены, словарь и настройки сайта; фонетика отдаётся из кода, не из таблиц. Демо-аккаунты не создаются. Если в БД ещё есть старые тестовые email (`demo@lumina.local`, `admin@lumina.local` и подобные), сидер удаляет только их — реальных пользователей не трогает. Админ из `ADMIN_EMAIL` / `ADMIN_PASSWORD` создаётся только если заданы обе переменные и такого email в БД ещё нет.

## Данные PostgreSQL

Файлы БД пишутся в `./data/postgres` на диске той машины, где запущен Compose (на сервере — папка рядом с проектом). Каталог в `.gitignore`, в git не попадает.

- `docker compose down` и перезапуск контейнеров **не** стирают уроки и пользователей.
- `docker compose down -v` **не** удаляет bind mount: чтобы стереть БД, нужно вручную удалить `data/postgres`.
- Бэкап: скопировать каталог `data/postgres` (лучше при остановленном сервисе `postgres`).

## Что внутри

- 76 грамматических модулей (A1–C2): урок → практика → тест
- 6 экзаменов уровней, проходной балл 75%
- 12 словарных тем с карточками, тренировкой и озвучкой
- Блок «Звуки»: таблица IPA, правила чтения, связная речь (10 тем)
- Прогресс, XP и серия дней
- Админка: пользователи, модули, упражнения, словарь, сводка

## Локальная разработка без Docker

1. Поднимите PostgreSQL и задайте `DATABASE_URL`.
2. `cd backend && pip install -r requirements.txt && python -m app.seed.runner && uvicorn app.main:app --reload`
3. `cd frontend && npm install && npm run dev`
