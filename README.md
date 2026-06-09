# 🧩 PostgreSQL Schema → Markdown Generator

Скрипт автоматически извлекает **структуру PostgreSQL базы данных** и формирует подробную Markdown-документацию (`database.md`).

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
| `public` | 10 | 107 | Общие таблицы |

---

### 📂 Схема: `public`

#### Таблицы схемы `public`

| Таблица | Назначение |
|----------|-------------|
| [comment](#publiccomment) | Вложения у комментариев |
| [sessions](#publicsessions) | Голосования |
| [votes](#publicvotes) | Все кто проголосовал |

#### `public.comment`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | nextval('public.comment_id_seq'::regclass) | Идентификатор |
| comment_id | bigint | ❌ | — | Комментарий |
| file_url | text | ❌ | — | Ссылка на файл |
| file_name | text | ❌ | — | Имя файла |
| created_at | timestamp | ✅ | now() | Дата создания |

---

## ⚙️ Возможности

- Подключается к PostgreSQL с использованием `psycopg2`;
- Извлекает только нужные схемы (например, `policyregistry`, `public`, `users_schema`);
- Поддерживает отдельные описания окружений `prod` и `stage` с разными подключениями и списками схем;
- Сохраняет Markdown с кликабельными якорями;
- Добавляет комментарии к таблицам, полям и функциям;
- Поддерживает PostgreSQL 12+.

---

## 🔧 Настройка окружений

`prod` остаётся совместимым с текущими переменными `DB_*`. Список схем прода задаётся через `PROD_DB_SCHEMAS`; если переменная не указана, используется список по умолчанию из `main.py`.

`stage` описывается отдельно через `STAGE_DB_*` и `STAGE_DB_SCHEMAS`. В `STAGE_DB_SCHEMAS` указывайте только те схемы, которые нужно добавить в документацию со стейджа:

```env
DB_HOST=prod-db.example.local
DB_PORT=5432
DB_NAME=ops
DB_USER=ops
DB_PASSWORD=change-me
PROD_DB_SCHEMAS=audit,cron,meritfund,migrations,policyregistry,users_schema

STAGE_DB_HOST=stage-db.example.local
STAGE_DB_PORT=5432
STAGE_DB_NAME=ops
STAGE_DB_USER=ops
STAGE_DB_PASSWORD=change-me
STAGE_DB_SCHEMAS=public,users_schema
```

Если `STAGE_DB_*` или `STAGE_DB_SCHEMAS` не заданы, stage-раздел пропускается.
