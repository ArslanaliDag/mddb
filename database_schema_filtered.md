# 🧩 Структура БД, включая схемы, таблицы и функции.

**СУБД:** PostgreSQL
**Дата обновления:** 28-01-2026

---

## 📚 Аудит голосований

- [Информация по аудиту](vote-sessions-audit.md)

---

## 🗄️ Миграции

- [Файлы миграций](Migrations/Success)

---

## ⏱️ Планировщик

- [Cron-задания](crone-database.md)

---
## 📂 Список схем

| Схема | Таблиц | Функций | Назначение |
|--------|---------|----------|----------|
| `audit` | 16 | 21 | Аудит |
| `migrations` | 1 | 0 | Миграции |
| `policyregistry` | 15 | 61 | Голосование |
| `users_schema` | 3 | 28 | Пользователи |

---
## 📂 Схема: `audit`

### Таблицы схемы `audit`
| Таблица | Назначение |
|----------|-------------|
| context_attributes_audit | Журналирование прав голосований |
| invites_audit | Журналирование приглашенных в голосование |
| options_audit | Журналирование вариантов выбора голосований |
| platform_attributes_audit | Журналирование прав доступа |
| user_platform_attribute_assignments_audit | Журналирование общих прав доступа |
| v_invite_user_joined | Определяет присоединившихся к голосованию участников |
| v_user_vote_changes | Определяет изменения голоса пользователя во времени |
| v_user_votes | Формирует факты голосования пользователей (одна строка = один выбор) |
| v_vote_results | Агрегированные результаты голосования |
| v_vote_session_events | Унифицированное представление всех audit-событий, относящихся к голосованию |
| v_vote_sessions_state_changes | Выделяет бизнес-значимые переходы состояний голосования |
| vote_business_events | Бизнес действия журналирования |
| vote_session_settings_audit | Журналирование настроек голосований |
| vote_sessions_audit | Журналирование голосований |
| vote_to_option_audit | Журналирование результатов голосования |
| votes_audit | Журналирование проголосовавших |

#### `audit.context_attributes_audit`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| operation_type | text | ❌ | — | — |
| app_user_id | bigint | ✅ | — | — |
| application_name | text | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ❌ | now() | — |
| old_data | jsonb | ✅ | — | — |
| new_data | jsonb | ✅ | — | — |

#### `audit.invites_audit`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| operation_type | text | ❌ | — | — |
| app_user_id | bigint | ✅ | — | — |
| application_name | text | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ❌ | now() | — |
| old_data | jsonb | ✅ | — | — |
| new_data | jsonb | ✅ | — | — |

#### `audit.options_audit`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| operation_type | text | ❌ | — | — |
| app_user_id | bigint | ✅ | — | — |
| application_name | text | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ❌ | now() | — |
| old_data | jsonb | ✅ | — | — |
| new_data | jsonb | ✅ | — | — |

#### `audit.platform_attributes_audit`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | ID |
| platform_attribute_id | integer | ✅ | — | Права доступа |
| title | text | ✅ | — | Название |
| description | text | ✅ | — | Описание |
| preferences_json | jsonb | ✅ | — | — |
| operation_type | text | ❌ | — | Тип операции |
| application_name | text | ✅ | — | Приложение |
| operation_timestamp | timestamp with time zone | ❌ | now() | Дата |
| old_data | jsonb | ✅ | — | Старые данные |
| new_data | jsonb | ✅ | — | Новые данные |
| app_user_id | bigint | ✅ | — | Пользователь |

#### `audit.user_platform_attribute_assignments_audit`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | ID |
| user_id | integer | ❌ | — | Кому дали права |
| platform_attribute_id | integer | ❌ | — | Права доступа |
| assigned_at | timestamp without time zone | ❌ | now() | Дата |
| operation_type | text | ❌ | — | Тип операции |
| application_name | text | ✅ | — | Приложение |
| operation_timestamp | timestamp with time zone | ❌ | now() | Дата |
| old_data | jsonb | ✅ | — | Старые данные |
| new_data | jsonb | ✅ | — | Новые данные |
| app_user_id | bigint | ✅ | — | Пользователь |

#### `audit.v_invite_user_joined`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| vote_session_id | bigint | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ✅ | — | — |
| joined_user_id | bigint | ✅ | — | — |

#### `audit.v_user_vote_changes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| vote_session_id | bigint | ✅ | — | — |
| app_user_id | bigint | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ✅ | — | — |
| old_option_id | text | ✅ | — | — |
| new_option_id | text | ✅ | — | — |

#### `audit.v_user_votes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| vote_session_id | bigint | ✅ | — | — |
| app_user_id | bigint | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ✅ | — | — |
| option_id | text | ✅ | — | — |

#### `audit.v_vote_results`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| vote_session_id | bigint | ✅ | — | — |
| option_id | integer | ✅ | — | — |
| option_title | character varying | ✅ | — | — |
| votes_count | bigint | ✅ | — | — |

#### `audit.v_vote_session_events`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| entity_type | text | ✅ | — | — |
| entity_id | bigint | ✅ | — | — |
| vote_session_id | bigint | ✅ | — | — |
| action | text | ✅ | — | — |
| old_data | jsonb | ✅ | — | — |
| new_data | jsonb | ✅ | — | — |
| app_user_id | bigint | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ✅ | — | — |

#### `audit.v_vote_sessions_state_changes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| audit_id | bigint | ✅ | — | — |
| vote_session_id | bigint | ✅ | — | — |
| event_type | text | ✅ | — | — |
| event_timestamp | timestamp with time zone | ✅ | — | — |
| app_user_id | bigint | ✅ | — | — |
| payload | jsonb | ✅ | — | — |

#### `audit.vote_business_events`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | nextval('audit.vote_business_events_id_seq'::regclass) | — |
| vote_session_id | bigint | ❌ | — | — |
| event_type | text | ❌ | — | — |
| event_timestamp | timestamp with time zone | ❌ | — | — |
| app_user_id | bigint | ✅ | — | — |
| payload | jsonb | ❌ | — | — |

#### `audit.vote_session_settings_audit`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| operation_type | text | ❌ | — | — |
| app_user_id | bigint | ✅ | — | — |
| application_name | text | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ❌ | now() | — |
| old_data | jsonb | ✅ | — | — |
| new_data | jsonb | ✅ | — | — |

#### `audit.vote_sessions_audit`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| operation_type | text | ❌ | — | — |
| app_user_id | bigint | ✅ | — | — |
| application_name | text | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ❌ | now() | — |
| old_data | jsonb | ✅ | — | — |
| new_data | jsonb | ✅ | — | — |

#### `audit.vote_to_option_audit`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| operation_type | text | ❌ | — | — |
| app_user_id | bigint | ✅ | — | — |
| application_name | text | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ❌ | now() | — |
| old_data | jsonb | ✅ | — | — |
| new_data | jsonb | ✅ | — | — |

#### `audit.votes_audit`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| operation_type | text | ❌ | — | — |
| app_user_id | bigint | ✅ | — | — |
| application_name | text | ✅ | — | — |
| operation_timestamp | timestamp with time zone | ❌ | now() | — |
| old_data | jsonb | ✅ | — | — |
| new_data | jsonb | ✅ | — | — |

### ⚙️ Функции схемы `audit`

#### `audit.fill_vote_business_events()` — возвращает `void`
Детерминированно пересобирает бизнес-журнал голосования на основе audit-логов

#### `audit.get_app_user_id()` — возвращает `bigint`
Получает пользоателя сделавшего действие

#### `audit.get_vote_sessions_business_markdown()` — возвращает `text`
Формирует человекочитаемый Markdown-журнал голосования для голосования

#### `audit.get_vote_sessions_full_markdown_log()` — возвращает `text`
Формирует Markdown-журнал полного аудита голосования (для админов)

#### `audit.human_action()` — возвращает `text`
Преобразует технические CRUD-действия в человекочитаемый вид

#### `audit.human_business_event()` — возвращает `text`
Преобразует машинные бизнес-события в человекочитаемый текст

#### `audit.human_entity()` — возвращает `text`
Преобразует технические имена сущностей в бизнес-термины

#### `audit.human_field_name()` — возвращает `text`
Человеческие названия полей для логов изменений

#### `audit.jsonb_diff()` — возвращает `TABLE(old_values jsonb, new_values jsonb)`
Определяет разницу между двумя JSONB объектами

#### `audit.resolve_field_value()` — возвращает `text`
Преобразует сырые значения полей в бизнес-читаемый формат

#### `audit.set_app_user_id()` — возвращает `void`
Устанавливает пользоателя сделавшего действие

#### `audit.tg_log_context_attributes()` — возвращает `trigger`
Триггер-функция действий над правами для голосования

#### `audit.tg_log_invites()` — возвращает `trigger`
Триггер-функция действий над присоединениями к голосованию

#### `audit.tg_log_options()` — возвращает `trigger`
Триггер-функция действий над вариантами голосования

#### `audit.tg_log_platform_attributes()` — возвращает `trigger`
Триггер-функция журналирование прав доступа

#### `audit.tg_log_user_platform_attribute_assignments()` — возвращает `trigger`
Триггер-функция журналирование общих прав доступа

#### `audit.tg_log_vote_session_settings()` — возвращает `trigger`
Триггер-функция действий над настройками голосования

#### `audit.tg_log_vote_sessions()` — возвращает `trigger`
Триггер-функция действий над самим голосованием

#### `audit.tg_log_vote_to_option()` — возвращает `trigger`
Триггер-функция действий над выборами голосующих

#### `audit.tg_log_votes()` — возвращает `trigger`
Триггер-функция действий над голосами

#### `audit.tg_on_vote_finished()` — возвращает `trigger`
Триггер-функция действий для завершением голосования

---
## 📂 Схема: `migrations`

### Таблицы схемы `migrations`
| Таблица | Назначение |
|----------|-------------|
| db_migrations | Центральная таблица со всеми миграциями в базе |

#### `migrations.db_migrations`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | integer | ❌ | nextval('migrations.db_migrations_id_seq'::regclass) | ID |
| migration_name | character varying | ❌ | — | Название |
| schema_name | character varying | ✅ | — | Схема |
| applied_at | timestamp without time zone | ✅ | CURRENT_TIMESTAMP | Дата |
| applied_by | character varying | ✅ | CURRENT_USER | Пользователь |
| execution_time_ms | integer | ✅ | — | Время выполнения |
| notes | text | ✅ | — | Примечание |
| migration_type | character varying | ✅ | — | Тип |

### ⚙️ Функции схемы `migrations`

_(нет функций)_

---
## 📂 Схема: `policyregistry`

### Таблицы схемы `policyregistry`
| Таблица | Назначение |
|----------|-------------|
| comment_attachments | Вложения (файлы) у комментариев |
| context_attributes | Права для голосования. Те кто могут голосовать, управлять голосованием |
| events | События связанные с голосованием |
| invites | Ссылка-приглашение для голосования |
| options | Опции (варианты выбора) в голосовании |
| platform_attributes | Права доступа (права Трибуны, права только для сервиса голосований) |
| structural_tags | Справочник структурных тегов |
| user_context_attribute_assignments | Выданные права пользователю в голосовании (добавленные пользователи к голосованияю) |
| user_platform_attribute_assignments | Общие права пользователя |
| vote_session_settings | Параметры голосования |
| vote_sessions | Голосования |
| vote_sessions_comments | Комментарии в голосовании |
| vote_sessions_structural_tags | Связующая таблица между голосованиями и структурными тегами |
| vote_to_option | Результаты голосования |
| votes | Все кто проголосовал |

#### `policyregistry.comment_attachments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | nextval('policyregistry.comment_attachments_id_seq'::regclass) | ID |
| comment_id | bigint | ❌ | — | Комментарий |
| file_url | text | ❌ | — | Ссылка |
| file_name | text | ❌ | — | Имя файла |
| created_at | timestamp without time zone | ✅ | now() | Дата |

#### `policyregistry.context_attributes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | ID |
| platform_attribute_id | bigint | ✅ | — | Права доступа |
| vote_session_id | bigint | ✅ | — | Голосование |
| title | character varying | ✅ | — | Название |
| description | text | ✅ | — | Описание |
| preferences_json | jsonb | ✅ | — | Настройки |

#### `policyregistry.events`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | nextval('policyregistry.events_id_seq'::regclass) | ID |
| created_at | timestamp without time zone | ✅ | now() | Дата |
| json | jsonb | ✅ | — | Настройки |
| is_read | boolean | ✅ | false | Прочтено(отработано) уведомление или нет |
| updated_at | timestamp with time zone | ✅ | now() | Дата обновления записи |
| title | character varying | ✅ | — | Название |

#### `policyregistry.invites`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | ID |
| vote_session_id | bigint | ❌ | — | Голосование |
| token | character varying | ❌ | — | Уникальная строка для построения ссылки |
| invited_by_id | bigint | ❌ | — | ID пользователя, который создал инвайт (внешний ключ на users_schema.users.id) |
| role | character varying | ❌ | 'voter'::character varying | Роль приглашенного (по умолчанию: voter) |
| max_uses | integer | ❌ | 1 | Максимальное количество использований инвайта |
| uses_count | integer | ❌ | 0 | Текущее количество использований инвайта |
| expires_at | timestamp without time zone | ✅ | — | Время окончания срока действия инвайта |
| created_at | timestamp without time zone | ✅ | now() | Дата |
| updated_at | timestamp without time zone | ✅ | now() | Дата обновления |
| invited_users_id | ARRAY | ✅ | '{}'::bigint[] | Массив ID пользователей, использовавших инвайт |
| enabled | boolean | ❌ | true | Флаг активности инвайта (true - активен, false - отключен) |

#### `policyregistry.options`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| title | character varying | ✅ | — | Название |
| vote_session_id | bigint | ❌ | — | Голосование |
| id | integer | ❌ | — | ID |

#### `policyregistry.platform_attributes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | ID |
| title | character varying | ✅ | — | Название |
| description | text | ✅ | — | Описание |
| preferences_json | jsonb | ✅ | — | Настройки |

#### `policyregistry.structural_tags`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| title | character varying | ❌ | — | Название структурного тега |
| is_deleted | boolean | ❌ | false | Флаг soft-delete |
| created_at | timestamp with time zone | ❌ | now() | Дата создания тега |
| link | character varying | ✅ | — | Ссылка на иконку команды (берется из s3 Шивы) |

#### `policyregistry.user_context_attribute_assignments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| user_id | bigint | ❌ | — | Пользователь |
| context_attribute_id | bigint | ❌ | — | Право голосования |
| assigned_at | timestamp without time zone | ✅ | — | ID |

#### `policyregistry.user_platform_attribute_assignments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| user_id | bigint | ❌ | — | Пользователь |
| platform_attribute_id | bigint | ❌ | — | Права |
| assigned_at | timestamp without time zone | ✅ | now() | ID |

#### `policyregistry.vote_session_settings`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| vote_session_id | bigint | ❌ | — | Голосование |
| data | jsonb | ✅ | — | Настройки |

#### `policyregistry.vote_sessions`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | ID |
| date_start | timestamp without time zone | ✅ | — | Дата начала |
| date_end | timestamp without time zone | ✅ | — | Дата конца |
| title | character varying | ✅ | — | Название |
| description | character varying | ✅ | — | Описание |
| type_config | jsonb | ✅ | — | Конфигурация |
| created_at | timestamp without time zone | ✅ | — | Дата |
| owner_id | bigint | ✅ | — | Владелец |
| type | integer | ✅ | — | Тип голосования |
| state | integer | ✅ | 0 | Статус |
| is_deleted | boolean | ❌ | false | Удалено или нет |

#### `policyregistry.vote_sessions_comments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | nextval('policyregistry.vote_sessions_comments_id_seq'::regclass) | ID |
| vote_session_id | bigint | ✅ | — | Голосование |
| user_id | bigint | ✅ | — | Пользователь |
| description | text | ✅ | — | Описание |
| created_at | timestamp without time zone | ✅ | now() | Дата |
| updated_at | timestamp without time zone | ✅ | now() | Дата обновления |

#### `policyregistry.vote_sessions_structural_tags`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| vote_session_id | bigint | ❌ | — | ID голосования |
| structural_tag_id | bigint | ❌ | — | ID структурного тега |
| created_at | timestamp with time zone | ❌ | now() | Дата привязки тега к голосованию |

#### `policyregistry.vote_to_option`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| option_id | integer | ❌ | — | Вариант в голосовании |
| weight | numeric | ✅ | — | Вес |
| vote_session_id | bigint | ❌ | — | Голосование |
| vote_id | character varying | ❌ | — | ID |

#### `policyregistry.votes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| user_id | bigint | ❌ | — | Пользоватлеь |
| vote_session_id | bigint | ❌ | — | Голосование |
| id | character varying | ❌ | — | ID |
| created_at | timestamp with time zone | ✅ | — | Дата |

### ⚙️ Функции схемы `policyregistry`

#### `policyregistry.archive_vote_session()` — возвращает `boolean`
Добавить голосование в архив с условиями

#### `policyregistry.assign_user_platform_attribute()` — возвращает `boolean`
Предоставить права доступа пользователю

#### `policyregistry.create_platform_attribute_json()` — возвращает `text`
Создание прав доступа

#### `policyregistry.create_structural_tag()` — возвращает `jsonb`
Теги голосования

#### `policyregistry.create_vote_session_comments()` — возвращает `jsonb`
Создает комментарий к голосованию с вложениями

#### `policyregistry.create_vote_session_invite()` — возвращает `jsonb`
Создает инвайт-ссылку для приглашения к голосованию

#### `policyregistry.create_vote_session_simple()` — возвращает `jsonb`
Создание голосоавния и заданий в pg_cron на старт и стоп голосоания

#### `policyregistry.cron_check_and_archive_vote_sessions()` — возвращает `void`
Находит все голосования, которые были удалены (is_deleted = true) и закончились больше 7 дней назад

#### `policyregistry.cron_notify_vote_sessions_reminder()` — возвращает `void`
Планирование напоминания за час всех голосующих о завершении голосования

#### `policyregistry.delete_comment_by_comment_id()` — возвращает `boolean`
Удалить комментарий к голосованию вместе с вложениями

#### `policyregistry.delete_platform_attribute()` — возвращает `boolean`
Удаление прав доступа

#### `policyregistry.delete_structural_tag()` — возвращает `boolean`
Деактивация структурного тега(soft-delete)

#### `policyregistry.delete_vote_session()` — возвращает `boolean`
Удаление голосования вместе со всеми задачами по голосованию в cron

#### `policyregistry.delete_vote_session_invite()` — возвращает `boolean`
Деактивировать инвайт к голосованию

#### `policyregistry.exist_create_shiva_task()` — возвращает `boolean`
Проверяет установлен ли парамет создания задачи в Шиве после завершения голосования

#### `policyregistry.exist_global_notify()` — возвращает `boolean`
Проверяет значение GlobalNotify - уведомлять ли голосующих или нет

#### `policyregistry.exists_platform_attribute()` — возвращает `boolean`
Есть ли права доступа или нет

#### `policyregistry.exists_vote_session()` — возвращает `boolean`
Существует ли голосование или нет

#### `policyregistry.fetch_and_delete_event()` — возвращает `json`
Пометить уведомление как прочтенное

#### `policyregistry.force_start_vote_session()` — возвращает `boolean`
Принудительный старт голосования

#### `policyregistry.force_stop_vote_session()` — возвращает `boolean`
Принудительнай остановка голосования

#### `policyregistry.generate_structural_tag_code()` — возвращает `character varying`
Генерация транслита из русских символов в латиницу

#### `policyregistry.get_all_platform_attributes_json()` — возвращает `text`
Получить все прав доступа

#### `policyregistry.get_all_vote_sessions_json()` — возвращает `jsonb`
Получить все голосования

#### `policyregistry.get_comment_by_comment_id()` — возвращает `jsonb`
Получает конкретный комментарий с вложениями в голосовании

#### `policyregistry.get_comments_by_vote_session_id()` — возвращает `jsonb`
Получает все комментарии и вложения по голосованию

#### `policyregistry.get_platform_attribute_json()` — возвращает `text`
Получить право доступа

#### `policyregistry.get_platform_attribute_user_ids_json()` — возвращает `text`
Получить тех кользователей у которых то или иное право

#### `policyregistry.get_result_with_winner_response_json()` — возвращает `jsonb`
Подсчет голосов по стратегиям выбора победителей голосования. Параметр стратегии выбора победителя не передается, вычисляется из таблицы policyregistry.vote_session_settings.data->>'ChoosingWinners'

#### `policyregistry.get_structural_tags()` — возвращает `jsonb`
Получить все структурные теги голосования

#### `policyregistry.get_user_context_attributes_json()` — возвращает `text`
Получить выданные права пользователя в голосовании

#### `policyregistry.get_user_platform_attributes_json()` — возвращает `text`
Получить права доступа пользователя

#### `policyregistry.get_vote_session_invite_by_token()` — возвращает `jsonb`
Получаем активное пригласительное по токену

#### `policyregistry.get_vote_session_invites()` — возвращает `jsonb`
Получить активные пригласительные на голосование у пользователя

#### `policyregistry.get_vote_session_json()` — возвращает `jsonb`
Получить информацию о голосовании

#### `policyregistry.get_vote_session_response_json()` — возвращает `jsonb`
Получить информацию о голосовании

#### `policyregistry.get_vote_sessions_by_count_json()` — возвращает `jsonb`
Получить определенное количество голосований

#### `policyregistry.get_vote_sessions_by_observer_json()` — возвращает `jsonb`
Получить все голосования в которых голосовал  Observers

#### `policyregistry.get_vote_sessions_by_owner_json()` — возвращает `jsonb`
Получить все голосования в которых голосовал  Owner

#### `policyregistry.get_vote_sessions_by_voter_json()` — возвращает `jsonb`
Получить все голосования в которых голосовал  Voter

#### `policyregistry.get_voted_count()` — возвращает `integer`
Получить количество проголосовавших в голосовании (именно проголосовавших, а не всех кто в голосовании)

#### `policyregistry.get_votes_statistics_jsonb()` — возвращает `jsonb`
Полня информация по результату голосования, кто за что голосовал из пользователей

#### `policyregistry.get_voting_result_response_json()` — возвращает `jsonb`
Получить результаты голосования

#### `policyregistry.is_user_platform_attribute_assigned()` — возвращает `boolean`
Назначены ли пользователю те или иные права

#### `policyregistry.list_sessions_with_scores_by_session_window()` — возвращает `jsonb`
Возвращает список голосования за заданный период времени вместе с итоговыми баллами по опциям

#### `policyregistry.list_sessions_with_votes_by_vote_time()` — возвращает `jsonb`
Возвращает список голосования за заданный период времени и для каждой — все голоса пользователей (по одному последнему голосу на пользователя) в виде JSONB.  В отличие от list_sessions_with_scores_by_session_window предыдущей функции (где считались итоговые баллы), здесь возвращаются сырые голоса.

#### `policyregistry.notify_vote_sessions()` — возвращает `void`
Сохраняет в events информацию о голосовании и отправляет уведомление

#### `policyregistry.notify_vote_sessions_reminder()` — возвращает `void`
Создает уведомления для напоминания всем участникам голосования за определенное время (час) до конца голосования

#### `policyregistry.tg_cron_notify_vote_sessions_reminder()` — возвращает `trigger`
Триггер-функция. Автоматически вызывается при создании или изменении голосования

#### `policyregistry.tg_notify_vote_sessions()` — возвращает `trigger`
Триггер-функция. Автоматически вызывается при обновлении поля state

#### `policyregistry.tg_update_updated_at_column()` — возвращает `trigger`
Генерация даты обновления поля updated_at

#### `policyregistry.unassign_user_platform_attribute()` — возвращает `boolean`
Удаление прав у пользователя

#### `policyregistry.update_comment_by_comment_id()` — возвращает `jsonb`
Обновляет комментарий и его вложения в голосовании

#### `policyregistry.update_platform_attribute_json()` — возвращает `boolean`
Обновление прав доступа

#### `policyregistry.update_structural_tag()` — возвращает `jsonb`
Обновление структурного тега голосования

#### `policyregistry.update_vote_session_invite()` — возвращает `jsonb`
Обновление приглашения к голосованию

#### `policyregistry.update_vote_session_simple_append()` — возвращает `jsonb`
Обновление голосования

#### `policyregistry.use_vote_session_invite()` — возвращает `boolean`
Используем приглашение в голосование. Добавление нового пользователя (присоединение) к голосованию при переходе по ссылки присоединиться

#### `policyregistry.user_has_voted()` — возвращает `boolean`
Проверка голосовал ли пользователь или нет (через votes)

#### `policyregistry.vote_id_hash()` — возвращает `text`
Для автоматического формирования идентификатора голоса (id) на основе пользователя и сессии голосования

#### `policyregistry.votes_set_id()` — возвращает `trigger`
Для автоматического формирования идентификатора голоса (id) на основе пользователя и сессии голосования

---
## 📂 Схема: `users_schema`

### Таблицы схемы `users_schema`
| Таблица | Назначение |
|----------|-------------|
| global_attributes | Команды (глобальные права всего Сенатора) |
| user_global_attribute_assignments | Пользователи в командах (глобальные права всего Сенатора) |
| users | Пользователи |

#### `users_schema.global_attributes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| title | character varying | ✅ | — | Название |
| description | text | ✅ | — | Описание |
| preferences_json | jsonb | ✅ | — | Настройки |
| shiva_id | bigint | ✅ | 0 | Айди Шивы (idTeam) |

#### `users_schema.user_global_attribute_assignments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| user_id | bigint | ❌ | — | Пользоватлеь |
| global_attribute_id | bigint | ❌ | — | Глобальные права |
| assigned_at | timestamp without time zone | ✅ | now() | — |

#### `users_schema.users`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| login | character varying | ❌ | — | Логин |
| firstname | character varying | ✅ | — | Имя |
| lastname | character varying | ✅ | — | Фамилия |
| emails | ARRAY | ✅ | — | Почта |
| discord | character varying | ✅ | — | Дискорд |
| tg | character varying | ✅ | — | Телеграм |
| not_sending | boolean | ❌ | false | — |
| controlcenter_id | bigint | ✅ | — | КонтролЦентр |
| avatar | bytea | ✅ | — | Аватарка |
| last_login_time | timestamp with time zone | ✅ | — | Дата и время последнего входа в систему пользователем |
| notify_data | jsonb | ✅ | '{"Email": 0, "Discord": 1, "Telegram": 0}'::jsonb | Куда уведомлять пользователя |
| avatar_s3 | character varying | ✅ | — | Ссылка на аватарку пользователя в s3 |

### ⚙️ Функции схемы `users_schema`

#### `users_schema.assign_user_global_attribute()` — возвращает `boolean`
Назначить глобальное право пользователю

#### `users_schema.create_global_attribute_json()` — возвращает `jsonb`
Создание глобального права

#### `users_schema.create_user_json()` — возвращает `jsonb`
Создание пользователя

#### `users_schema.create_users_from_json()` — возвращает `None`
Создание или обновление (если существует) пользователя

#### `users_schema.delete_global_attribute()` — возвращает `boolean`
Удаление глобальных прав

#### `users_schema.delete_user()` — возвращает `boolean`
Удаление пользователя

#### `users_schema.exists_global_attribute()` — возвращает `boolean`
Есть ли такие глобальные права или нет

#### `users_schema.exists_user()` — возвращает `boolean`
Существует пользователь или нет

#### `users_schema.get_all_global_attributes_json()` — возвращает `jsonb`
Получить все глобальные атрибуты

#### `users_schema.get_all_users_json()` — возвращает `jsonb`
Получить всех пользователей

#### `users_schema.get_controlcenter_differences()` — возвращает `TABLE(firstname text, lastname text, login text, json_user_id bigint, db_controlcenter_id bigint)`
Поиск расхождений между пользователями, указанными в JSON массиве (пользователи КонтрлЦентра), и пользователями в таблице users_schema.users

#### `users_schema.get_controlcenter_new_users()` — возвращает `TABLE(firstname text, lastname text, login text, json_user_id bigint)`
Проверяет есть ли пользователи из массива в таблице users

#### `users_schema.get_global_attribute_json()` — возвращает `jsonb`
Получить глобальные атрибуты

#### `users_schema.get_global_attribute_user_ids_json()` — возвращает `jsonb`
Получить пользователей у которых есть то или иное право

#### `users_schema.get_global_attributes_with_users()` — возвращает `jsonb`
Возвращает иерархическую структуру команда → список пользователей для визуализации

#### `users_schema.get_user_by_cc_json()` — возвращает `jsonb`
Получаем данные о вошедшем пользователе в систему и обновляем дату последнего визита

#### `users_schema.get_user_by_login_json()` — возвращает `jsonb`
Получить пользователя по логину

#### `users_schema.get_user_cc_id_json()` — возвращает `jsonb`
Получить controlcenter_id пользователя

#### `users_schema.get_user_global_attributes_json()` — возвращает `jsonb`
Получить глобальные права пользователя

#### `users_schema.get_user_ids_by_discords()` — возвращает `jsonb`
Получает пользовательские айди по дискорду

#### `users_schema.get_user_json()` — возвращает `jsonb`
Получить пользователя

#### `users_schema.is_user_global_attribute_assigned()` — возвращает `boolean`
Проверяет есть ли у пользователя те или иные глобальные права

#### `users_schema.sp_assign_team_attributes()` — возвращает `None`
Cоздаёт атрибуты команд, если их ещё нет и назначает эти атрибуты пользователям, сопоставляя их по имени и фамилии. Работает идемпотентно — повторный запуск не создаёт дублей

#### `users_schema.unassign_user_global_attribute()` — возвращает `boolean`
Забрать права у пользователя

#### `users_schema.update_global_attribute_json()` — возвращает `boolean`
Обновление глобальных атрибутов

#### `users_schema.update_user_json()` — возвращает `boolean`
Обновление пользоателя

#### `users_schema.user_row_to_json()` — возвращает `jsonb`
Преобразует таблицу users в объект json

#### `users_schema.users_mute_simple()` — возвращает `void`
—

---