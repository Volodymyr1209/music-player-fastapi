# 🎵 Music Player API

Music Player API — це вебзастосунок для завантаження, зберігання та відтворення музичних треків, розроблений з використанням FastAPI, PostgreSQL та Docker.

Проєкт створений як навчальна система керування музичною бібліотекою та демонструє сучасний підхід до розробки Backend-додатків із використанням REST API, контейнеризації та реляційних баз даних.

---

# 🚀 Основні можливості

### 🎵 Робота з треками

* Завантаження MP3 файлів
* Збереження інформації про треки в PostgreSQL
* Отримання списку треків через API
* Відтворення музики через браузер
* Зберігання музичних файлів на сервері

### 🌐 Вебплеєр

* Відображення списку треків
* Вбудований HTML5 аудіоплеєр
* Перемикання між треками
* Автоматичне відтворення наступного треку
* Сучасний інтерфейс у стилі Spotify

### 📦 API

* REST API на базі FastAPI
* Автоматична Swagger документація
* OpenAPI Specification
* JSON відповіді

### 🐳 Docker

* Контейнеризація застосунку
* Окремий контейнер для PostgreSQL
* Docker Compose для запуску всієї системи

---

# 🛠️ Використані технології

## Backend

* Python 3.11
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

## Database

* PostgreSQL 15

## Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates

## DevOps

* Docker
* Docker Compose

## Version Control

* Git
* GitHub

---

# 📂 Структура проєкту

```text
music-player/
│
├── database/
│   ├── database.py
│   └── session.py
│
├── models/
│   ├── artist.py
│   ├── album.py
│   ├── track.py
│   ├── playlist.py
│   └── user.py
│
├── routers/
│   └── tracks.py
│
├── schemas/
│   └── track.py
│
├── services/
│   └── tracks.py
│
├── templates/
│   └── player.html
│
├── uploads/
│   └── music/
│
├── alembic/
│
├── main.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

---

# 🗄️ Структура бази даних

Проєкт використовує PostgreSQL для зберігання інформації про користувачів, виконавців, альбоми, треки та плейлисти.

---

## Таблиця users

| Поле          | Тип       |
| ------------- | --------- |
| id            | UUID      |
| username      | VARCHAR   |
| email         | VARCHAR   |
| password_hash | VARCHAR   |
| created_at    | TIMESTAMP |

---

## Таблиця artists

| Поле       | Тип       |
| ---------- | --------- |
| id         | UUID      |
| name       | VARCHAR   |
| country    | VARCHAR   |
| created_at | TIMESTAMP |

---

## Таблиця albums

| Поле         | Тип       |
| ------------ | --------- |
| id           | UUID      |
| title        | VARCHAR   |
| release_year | INTEGER   |
| artist_id    | UUID      |
| created_at   | TIMESTAMP |

---

## Таблиця tracks

| Поле       | Тип       |
| ---------- | --------- |
| id         | UUID      |
| title      | VARCHAR   |
| album_id   | UUID      |
| genre      | VARCHAR   |
| duration   | INTEGER   |
| file_path  | VARCHAR   |
| created_at | TIMESTAMP |

---

## Таблиця playlists

| Поле        | Тип       |
| ----------- | --------- |
| id          | UUID      |
| name        | VARCHAR   |
| description | TEXT      |
| user_id     | UUID      |
| created_at  | TIMESTAMP |

---

## Таблиця playlist_tracks

| Поле        | Тип  |
| ----------- | ---- |
| playlist_id | UUID |
| track_id    | UUID |

---

# 🔗 Зв'язки між таблицями

```text
Artist 1 ---- N Album

Album 1 ---- N Track

User 1 ---- N Playlist

Playlist N ---- N Track
```

---

# 📡 API Endpoints

## Отримати всі треки

```http
GET /tracks/
```

Повертає список усіх треків.

---

## Вебплеєр

```http
GET /tracks/player
```

Відкриває вебінтерфейс музичного плеєра.

---

## Відтворити трек

```http
GET /tracks/{track_id}/play
```

Повертає MP3 файл для відтворення.

---

## Завантажити трек

```http
POST /tracks/upload
```

Параметри:

* title
* album_id
* genre
* duration
* file

---

# 🐳 Docker

## Побудова контейнерів

```bash
docker compose build
```

## Запуск системи

```bash
docker compose up -d
```

## Зупинка системи

```bash
docker compose down
```

## Перегляд контейнерів

```bash
docker compose ps
```

---

# 🌐 Доступ до застосунку

### Swagger UI

```text
http://localhost:8000/docs
```

### Music Player

```text
http://localhost:8000/tracks/player
```

---

# 🎯 Реалізовано

✅ Завантаження MP3 файлів

✅ Збереження даних у PostgreSQL

✅ Відтворення музики

✅ HTML Music Player

✅ Docker контейнеризація

✅ Swagger документація

✅ SQLAlchemy ORM

✅ PostgreSQL інтеграція

---

# Майбутні покращення

* Авторизація користувачів
* Реєстрація користувачів
* Керування виконавцями
* Керування альбомами
* Створення плейлистів
* Видалення треків
* Пошук музики
* Обкладинки альбомів
* Улюблені треки
* Рекомендаційна система

---

# 👨‍💻 Автор

**Volodymyr Yaniuk**



Розроблено з використанням FastAPI, PostgreSQL та Docker.
