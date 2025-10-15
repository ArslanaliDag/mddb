# 🧩 PostgreSQL Schema → Markdown Generator

Скрипт автоматически извлекает **структуру PostgreSQL базы данных** и формирует подробную Markdown-документацию (`database_schema.md`).

Документация включает:
- ✅ список схем с количеством таблиц и функций;
- ✅ таблицы с их назначением (из комментариев к таблицам);
- ✅ детальную структуру каждой таблицы (поля, типы, nullable, default, комментарии);
- ✅ список функций схем с типом возвращаемого значения и описанием;
- ✅ кликабельные ссылки на таблицы и функции внутри документа.

---

## 📦 Пример результата

### 📂 Список схем

| Схема | Таблиц | Функций | Назначение |
|--------|---------|----------|-------------|
| `policyregistry` | 9 | 33 | Голосование |
| `public` | 10 | 107 | Общие таблицы |
| `users_schema` | 3 | 24 | Пользователи |

---

### 📂 Схема: `policyregistry`

#### Таблицы схемы `policyregistry`

| Таблица | Назначение |
|----------|-------------|
| [comment_attachments](#policyregistrycommentattachments) | Вложения (файлы) у комментариев |
| [vote_sessions](#policyregistryvotesessions) | Голосования |
| [votes](#policyregistryvotes) | Все кто проголосовал |

#### `policyregistry.comment_attachments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | nextval('policyregistry.comment_attachments_id_seq'::regclass) | Идентификатор |
| comment_id | bigint | ❌ | — | Комментарий |
| file_url | text | ❌ | — | Ссылка на файл |
| file_name | text | ❌ | — | Имя файла |
| created_at | timestamp | ✅ | now() | Дата создания |

---

## ⚙️ Возможности

- Подключается к PostgreSQL с использованием `psycopg2`;
- Извлекает только нужные схемы (например, `policyregistry`, `public`, `users_schema`);
- Сохраняет Markdown с кликабельными якорями;
- Добавляет комментарии к таблицам, полям и функциям;
- Поддерживает PostgreSQL 12+.

---