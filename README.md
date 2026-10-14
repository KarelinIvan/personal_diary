📅 Personal Diary — Личный дневник

Учебный проект (дипломная работа) по курсу «Python Backend Developer» от Skypro. Веб-приложение для ведения личного блога на Django.

Основные функции:
- CRUD: Создание, просмотр, обновление и удаление записей (CreateView, UpdateView и др.).
- Изоляция данных: пользователь видит только свои записи благодаря фильтрации в методе get_queryset.
- Поиск: реализация поиска по заголовку или содержимому статьи через ORM Django (Q объекты).
- Пагинация: вывод 5 записей на страницу для удобства чтения.

✨ Технологии (Стек)
- Backend: Python 3.12+, Django 5.1+
- Базы данных: PostgreSQL
- Инфраструктура: Docker, Docker Compose
- Документация: Swagger (drf-yasg) не реализована, но API интуитивно понятен.
- Инструменты: Poetry (pyproject.toml), Pytest (coverage).

🚀 Запуск проекта

Через Docker (рекомендуется)
- Скопируйте файл `.env.example`
- Запустите контейнеры: docker-compose up --build

Проект откроется автоматически по адресу http://localhost, либо используйте админ-панель Django: http://localhost/admin/

Локальный запуск (с Poetry)
- Клонируйте репозиторий: git clone https://github.com/KarelinIvan/personal_diary.git
- Создайте виртуальное окружение и установите зависимости: poetry install
- Примените миграции базы данных: python manage.py migrate
- Создайте суперюзера для админки: python manage.py createsuperuser
- Запустите сервер разработки: python manage.py runserver

Проект откроется автоматически по адресу http://127.0.0.1:8000, либо используйте админ-панель Django: http://127.0.0.1:8000/admin/
