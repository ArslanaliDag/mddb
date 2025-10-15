# 🧩 Структура БД, включая схемы, таблицы и функции.

**СУБД:** PostgreSQL
**Дата обновления:** 15-10-2025
---
## 📂 Список схем

| Схема | Таблиц | Функций | Назначение |
|--------|---------|----------|----------|
| `policyregistry` | 12 | 44 | Голосование |
| `public` | 10 | 107 | Общая |
| `users_schema` | 3 | 24 | Пользователи |

---
## 📂 Схема: `policyregistry`

### Таблицы схемы `policyregistry`
| Таблица | Назначение |
|----------|-------------|
| comment_attachments | Вложения (файлы) у комментариев |
| context_attributes | Права для голосования. Те кто могут голосовать, управлять голосованием |
| events | События связанные с голосованием |
| options | Опции (варианты выбора) в голосовании |
| platform_attributes | Общие права |
| user_context_attribute_assignments | Выданные права пользователю в голосовании |
| user_platform_attribute_assignments | Общие права пользователя |
| vote_session_settings | Параметры голосования |
| vote_sessions | Голосования |
| vote_sessions_comments | Комментарии в голосовании |
| vote_to_option | Результаты голосования |
| votes | Все кто проголосовал |

#### `policyregistry.comment_attachments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | nextval('policyregistry.comment_attachments_id_seq'::regclass) | — |
| comment_id | bigint | ❌ | — | — |
| file_url | text | ❌ | — | — |
| file_name | text | ❌ | — | — |
| created_at | timestamp without time zone | ✅ | now() | — |

#### `policyregistry.context_attributes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| platform_attribute_id | bigint | ✅ | — | — |
| vote_session_id | bigint | ✅ | — | — |
| title | character varying | ✅ | — | — |
| description | text | ✅ | — | — |
| preferences_json | jsonb | ✅ | — | — |

#### `policyregistry.events`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | nextval('policyregistry.events_id_seq'::regclass) | — |
| created_at | timestamp without time zone | ✅ | now() | — |
| json | jsonb | ✅ | — | — |

#### `policyregistry.options`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| title | character varying | ✅ | — | — |
| vote_session_id | bigint | ❌ | — | — |
| id | integer | ❌ | — | — |

#### `policyregistry.platform_attributes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| title | character varying | ✅ | — | — |
| description | text | ✅ | — | — |
| preferences_json | jsonb | ✅ | — | — |

#### `policyregistry.user_context_attribute_assignments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| user_id | bigint | ❌ | — | — |
| context_attribute_id | bigint | ❌ | — | — |
| assigned_at | timestamp without time zone | ✅ | — | — |

#### `policyregistry.user_platform_attribute_assignments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| user_id | bigint | ❌ | — | — |
| platform_attribute_id | bigint | ❌ | — | — |
| assigned_at | timestamp without time zone | ✅ | — | — |

#### `policyregistry.vote_session_settings`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| vote_session_id | bigint | ❌ | — | — |
| data | jsonb | ✅ | — | — |

#### `policyregistry.vote_sessions`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| date_start | timestamp without time zone | ✅ | — | — |
| date_end | timestamp without time zone | ✅ | — | — |
| title | character varying | ✅ | — | — |
| description | character varying | ✅ | — | — |
| type_config | jsonb | ✅ | — | — |
| created_at | timestamp without time zone | ✅ | — | — |
| owner_id | bigint | ✅ | — | — |
| type | integer | ✅ | — | — |
| state | integer | ✅ | 0 | — |
| is_deleted | boolean | ❌ | false | — |

#### `policyregistry.vote_sessions_comments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | nextval('policyregistry.vote_sessions_comments_id_seq'::regclass) | — |
| vote_session_id | bigint | ✅ | — | — |
| user_id | bigint | ✅ | — | — |
| description | text | ✅ | — | — |
| created_at | timestamp without time zone | ✅ | now() | — |
| updated_at | timestamp without time zone | ✅ | now() | — |

#### `policyregistry.vote_to_option`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| option_id | integer | ❌ | — | — |
| weight | numeric | ✅ | — | — |
| vote_session_id | bigint | ❌ | — | — |
| vote_id | character varying | ❌ | — | — |

#### `policyregistry.votes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| user_id | bigint | ❌ | — | — |
| vote_session_id | bigint | ❌ | — | — |
| id | character varying | ❌ | — | — |

### ⚙️ Функции схемы `policyregistry`

#### `policyregistry.add_observers()` — возвращает `boolean`
—

#### `policyregistry.add_voters()` — возвращает `boolean`
—

#### `policyregistry.assign_user_platform_attribute()` — возвращает `boolean`
—

#### `policyregistry.create_platform_attribute_json()` — возвращает `text`
—

#### `policyregistry.create_vote_session_comments()` — возвращает `jsonb`
Создает комментарий к голосованию с вложениями

#### `policyregistry.create_vote_session_simple()` — возвращает `jsonb`
Создание голосоавния и заданий в pg_cron на старт и стоп голосоания

#### `policyregistry.cron_notify_vote_sessions_reminder()` — возвращает `void`
Планирование напоминания за определенное время (час) всех голосующих о завершении голосования

#### `policyregistry.delete_comment_by_comment_id()` — возвращает `boolean`
Удалить комментарий к голосованию вместе с вложениями

#### `policyregistry.delete_platform_attribute()` — возвращает `boolean`
Удаляет платформенный атрибут по ID

#### `policyregistry.delete_vote_session()` — возвращает `boolean`
Удаление голосования

#### `policyregistry.exists_platform_attribute()` — возвращает `boolean`
—

#### `policyregistry.exists_vote_session()` — возвращает `boolean`
—

#### `policyregistry.fetch_and_delete_event()` — возвращает `json`
—

#### `policyregistry.get_all_platform_attributes_json()` — возвращает `text`
—

#### `policyregistry.get_all_vote_sessions_json()` — возвращает `jsonb`
—

#### `policyregistry.get_comment_by_comment_id()` — возвращает `jsonb`
Получает конкретный комментарий с вложениями в голосовании

#### `policyregistry.get_comments_by_vote_session_id()` — возвращает `jsonb`
Получает все комментарии и вложения по голосованию

#### `policyregistry.get_platform_attribute_json()` — возвращает `text`
—

#### `policyregistry.get_platform_attribute_user_ids_json()` — возвращает `text`
—

#### `policyregistry.get_result_with_winner_response_json()` — возвращает `jsonb`
Подсчет голосов по стратегиям выбора победителей голосования. Параметр стратегии выбора победителя не передается, вычисляется из таблицы policyregistry.vote_session_settings.data->>'ChoosingWinners'

#### `policyregistry.get_result_with_winner_response_json_temp()` — возвращает `jsonb`
Подсчет голосов по стратегиям выбора победителей голосования. Параметр стратегии выбора победителя передается текстом.

#### `policyregistry.get_result_with_winner_response_json_temp2()` — возвращает `jsonb`
—

#### `policyregistry.get_user_context_attributes_json()` — возвращает `text`
—

#### `policyregistry.get_user_platform_attributes_json()` — возвращает `text`
—

#### `policyregistry.get_vote_session_json()` — возвращает `jsonb`
Получить информацию о голосовании

#### `policyregistry.get_vote_session_response_json()` — возвращает `jsonb`
—

#### `policyregistry.get_vote_sessions_by_count_json()` — возвращает `jsonb`
—

#### `policyregistry.get_vote_sessions_by_observer_json()` — возвращает `jsonb`
—

#### `policyregistry.get_vote_sessions_by_owner_json()` — возвращает `jsonb`
—

#### `policyregistry.get_vote_sessions_by_voter_json()` — возвращает `jsonb`
—

#### `policyregistry.get_voting_result_response_json()` — возвращает `jsonb`
—

#### `policyregistry.is_user_platform_attribute_assigned()` — возвращает `boolean`
—

#### `policyregistry.list_sessions_with_scores_by_session_window()` — возвращает `jsonb`
—

#### `policyregistry.list_sessions_with_votes_by_vote_time()` — возвращает `jsonb`
—

#### `policyregistry.notify_vote_sessions()` — возвращает `void`
Сохраняет в events информацию о голосовании и отправляет уведомление

#### `policyregistry.notify_vote_sessions_reminder()` — возвращает `void`
Создает уведомления для напоминания всем участникам голосования за определенное время (час) до конца голосования

#### `policyregistry.tg_cron_notify_vote_sessions_reminder()` — возвращает `trigger`
Триггер-функция. Автоматически вызывается при создании или изменении голосования

#### `policyregistry.tg_notify_vote_sessions()` — возвращает `trigger`
Триггер-функция. Автоматически вызывается при обновлении поля state

#### `policyregistry.unassign_user_platform_attribute()` — возвращает `boolean`
—

#### `policyregistry.update_comment_by_comment_id()` — возвращает `jsonb`
Обновляет комментарий и его вложения в голосовании

#### `policyregistry.update_platform_attribute_json()` — возвращает `boolean`
—

#### `policyregistry.update_vote_session_simple_append()` — возвращает `jsonb`
Обновление голосования

#### `policyregistry.vote_id_hash()` — возвращает `text`
—

#### `policyregistry.votes_set_id()` — возвращает `trigger`
—

---
## 📂 Схема: `public`

### Таблицы схемы `public`
| Таблица | Назначение |
|----------|-------------|
| backups | — |
| databases | — |
| destinations | — |
| executions | — |
| goose_db_version | — |
| restorations | — |
| sessions | — |
| users | — |
| webhook_executions | — |
| webhooks | — |

#### `public.backups`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | uuid | ❌ | uuid_generate_v4() | — |
| database_id | uuid | ❌ | — | — |
| destination_id | uuid | ✅ | — | — |
| name | text | ❌ | — | — |
| cron_expression | text | ❌ | — | — |
| time_zone | text | ❌ | — | — |
| is_active | boolean | ❌ | false | — |
| dest_dir | text | ❌ | — | — |
| retention_days | smallint | ❌ | 0 | — |
| opt_data_only | boolean | ❌ | false | — |
| opt_schema_only | boolean | ❌ | false | — |
| opt_clean | boolean | ❌ | false | — |
| opt_if_exists | boolean | ❌ | false | — |
| opt_create | boolean | ❌ | false | — |
| opt_no_comments | boolean | ❌ | false | — |
| created_at | timestamp with time zone | ❌ | now() | — |
| updated_at | timestamp with time zone | ✅ | — | — |
| is_local | boolean | ❌ | false | — |

#### `public.databases`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | uuid | ❌ | uuid_generate_v4() | — |
| name | text | ❌ | — | — |
| connection_string | bytea | ❌ | — | — |
| pg_version | text | ❌ | — | — |
| created_at | timestamp with time zone | ❌ | now() | — |
| updated_at | timestamp with time zone | ✅ | — | — |
| test_ok | boolean | ✅ | — | — |
| test_error | text | ✅ | — | — |
| last_test_at | timestamp with time zone | ✅ | — | — |

#### `public.destinations`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | uuid | ❌ | uuid_generate_v4() | — |
| name | text | ❌ | — | — |
| bucket_name | text | ❌ | — | — |
| access_key | bytea | ❌ | — | — |
| secret_key | bytea | ❌ | — | — |
| region | text | ❌ | — | — |
| endpoint | text | ❌ | — | — |
| created_at | timestamp with time zone | ❌ | now() | — |
| updated_at | timestamp with time zone | ✅ | — | — |
| test_ok | boolean | ✅ | — | — |
| test_error | text | ✅ | — | — |
| last_test_at | timestamp with time zone | ✅ | — | — |

#### `public.executions`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | uuid | ❌ | uuid_generate_v4() | — |
| backup_id | uuid | ❌ | — | — |
| status | text | ❌ | 'running'::text | — |
| message | text | ✅ | — | — |
| path | text | ✅ | — | — |
| started_at | timestamp with time zone | ❌ | now() | — |
| updated_at | timestamp with time zone | ✅ | — | — |
| finished_at | timestamp with time zone | ✅ | — | — |
| deleted_at | timestamp with time zone | ✅ | — | — |
| file_size | bigint | ✅ | — | — |

#### `public.goose_db_version`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | integer | ❌ | — | — |
| version_id | bigint | ❌ | — | — |
| is_applied | boolean | ❌ | — | — |
| tstamp | timestamp without time zone | ❌ | now() | — |

#### `public.restorations`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | uuid | ❌ | uuid_generate_v4() | — |
| execution_id | uuid | ❌ | — | — |
| database_id | uuid | ✅ | — | — |
| status | text | ❌ | 'running'::text | — |
| message | text | ✅ | — | — |
| started_at | timestamp with time zone | ❌ | now() | — |
| updated_at | timestamp with time zone | ✅ | — | — |
| finished_at | timestamp with time zone | ✅ | — | — |

#### `public.sessions`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | uuid | ❌ | uuid_generate_v4() | — |
| user_id | uuid | ❌ | — | — |
| token | bytea | ❌ | — | — |
| ip | text | ❌ | — | — |
| user_agent | text | ❌ | — | — |
| created_at | timestamp with time zone | ❌ | now() | — |

#### `public.users`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | uuid | ❌ | uuid_generate_v4() | — |
| name | text | ❌ | — | — |
| email | text | ❌ | — | — |
| password | text | ❌ | — | — |
| created_at | timestamp with time zone | ❌ | now() | — |
| updated_at | timestamp with time zone | ✅ | — | — |

#### `public.webhook_executions`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | uuid | ❌ | uuid_generate_v4() | — |
| webhook_id | uuid | ❌ | — | — |
| req_method | text | ✅ | — | — |
| req_headers | text | ✅ | — | — |
| req_body | text | ✅ | — | — |
| res_status | smallint | ✅ | — | — |
| res_headers | text | ✅ | — | — |
| res_body | text | ✅ | — | — |
| res_duration | integer | ✅ | — | — |
| created_at | timestamp with time zone | ❌ | now() | — |

#### `public.webhooks`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | uuid | ❌ | uuid_generate_v4() | — |
| name | text | ❌ | — | — |
| is_active | boolean | ❌ | false | — |
| event_type | text | ❌ | — | — |
| target_ids | ARRAY | ❌ | — | — |
| url | text | ❌ | — | — |
| method | text | ❌ | — | — |
| headers | text | ✅ | — | — |
| body | text | ✅ | — | — |
| created_at | timestamp with time zone | ❌ | now() | — |
| updated_at | timestamp with time zone | ✅ | — | — |

### ⚙️ Функции схемы `public`

#### `public.akeys()` — возвращает `text[]`
—

#### `public.armor()` — возвращает `text`
—

#### `public.armor()` — возвращает `text`
—

#### `public.avals()` — возвращает `text[]`
—

#### `public.change_updated_at()` — возвращает `trigger`
—

#### `public.crypt()` — возвращает `text`
—

#### `public.dearmor()` — возвращает `bytea`
—

#### `public.decrypt()` — возвращает `bytea`
—

#### `public.decrypt_iv()` — возвращает `bytea`
—

#### `public.defined()` — возвращает `boolean`
—

#### `public.delete()` — возвращает `hstore`
—

#### `public.delete()` — возвращает `hstore`
—

#### `public.delete()` — возвращает `hstore`
—

#### `public.digest()` — возвращает `bytea`
—

#### `public.digest()` — возвращает `bytea`
—

#### `public.each()` — возвращает `SETOF record`
—

#### `public.encrypt()` — возвращает `bytea`
—

#### `public.encrypt_iv()` — возвращает `bytea`
—

#### `public.exist()` — возвращает `boolean`
—

#### `public.exists_all()` — возвращает `boolean`
—

#### `public.exists_any()` — возвращает `boolean`
—

#### `public.fetchval()` — возвращает `text`
—

#### `public.gen_random_bytes()` — возвращает `bytea`
—

#### `public.gen_random_uuid()` — возвращает `uuid`
—

#### `public.gen_salt()` — возвращает `text`
—

#### `public.gen_salt()` — возвращает `text`
—

#### `public.ghstore_compress()` — возвращает `internal`
—

#### `public.ghstore_consistent()` — возвращает `boolean`
—

#### `public.ghstore_decompress()` — возвращает `internal`
—

#### `public.ghstore_in()` — возвращает `ghstore`
—

#### `public.ghstore_options()` — возвращает `void`
—

#### `public.ghstore_out()` — возвращает `cstring`
—

#### `public.ghstore_penalty()` — возвращает `internal`
—

#### `public.ghstore_picksplit()` — возвращает `internal`
—

#### `public.ghstore_same()` — возвращает `internal`
—

#### `public.ghstore_union()` — возвращает `ghstore`
—

#### `public.gin_consistent_hstore()` — возвращает `boolean`
—

#### `public.gin_extract_hstore()` — возвращает `internal`
—

#### `public.gin_extract_hstore_query()` — возвращает `internal`
—

#### `public.hmac()` — возвращает `bytea`
—

#### `public.hmac()` — возвращает `bytea`
—

#### `public.hs_concat()` — возвращает `hstore`
—

#### `public.hs_contained()` — возвращает `boolean`
—

#### `public.hs_contains()` — возвращает `boolean`
—

#### `public.hstore()` — возвращает `hstore`
—

#### `public.hstore()` — возвращает `hstore`
—

#### `public.hstore()` — возвращает `hstore`
—

#### `public.hstore()` — возвращает `hstore`
—

#### `public.hstore_cmp()` — возвращает `integer`
—

#### `public.hstore_eq()` — возвращает `boolean`
—

#### `public.hstore_ge()` — возвращает `boolean`
—

#### `public.hstore_gt()` — возвращает `boolean`
—

#### `public.hstore_hash()` — возвращает `integer`
—

#### `public.hstore_hash_extended()` — возвращает `bigint`
—

#### `public.hstore_in()` — возвращает `hstore`
—

#### `public.hstore_le()` — возвращает `boolean`
—

#### `public.hstore_lt()` — возвращает `boolean`
—

#### `public.hstore_ne()` — возвращает `boolean`
—

#### `public.hstore_out()` — возвращает `cstring`
—

#### `public.hstore_recv()` — возвращает `hstore`
—

#### `public.hstore_send()` — возвращает `bytea`
—

#### `public.hstore_subscript_handler()` — возвращает `internal`
—

#### `public.hstore_to_array()` — возвращает `text[]`
—

#### `public.hstore_to_json()` — возвращает `json`
—

#### `public.hstore_to_json_loose()` — возвращает `json`
—

#### `public.hstore_to_jsonb()` — возвращает `jsonb`
—

#### `public.hstore_to_jsonb_loose()` — возвращает `jsonb`
—

#### `public.hstore_to_matrix()` — возвращает `text[]`
—

#### `public.hstore_version_diag()` — возвращает `integer`
—

#### `public.isdefined()` — возвращает `boolean`
—

#### `public.isexists()` — возвращает `boolean`
—

#### `public.pgp_armor_headers()` — возвращает `SETOF record`
—

#### `public.pgp_key_id()` — возвращает `text`
—

#### `public.pgp_pub_decrypt()` — возвращает `text`
—

#### `public.pgp_pub_decrypt()` — возвращает `text`
—

#### `public.pgp_pub_decrypt()` — возвращает `text`
—

#### `public.pgp_pub_decrypt_bytea()` — возвращает `bytea`
—

#### `public.pgp_pub_decrypt_bytea()` — возвращает `bytea`
—

#### `public.pgp_pub_decrypt_bytea()` — возвращает `bytea`
—

#### `public.pgp_pub_encrypt()` — возвращает `bytea`
—

#### `public.pgp_pub_encrypt()` — возвращает `bytea`
—

#### `public.pgp_pub_encrypt_bytea()` — возвращает `bytea`
—

#### `public.pgp_pub_encrypt_bytea()` — возвращает `bytea`
—

#### `public.pgp_sym_decrypt()` — возвращает `text`
—

#### `public.pgp_sym_decrypt()` — возвращает `text`
—

#### `public.pgp_sym_decrypt_bytea()` — возвращает `bytea`
—

#### `public.pgp_sym_decrypt_bytea()` — возвращает `bytea`
—

#### `public.pgp_sym_encrypt()` — возвращает `bytea`
—

#### `public.pgp_sym_encrypt()` — возвращает `bytea`
—

#### `public.pgp_sym_encrypt_bytea()` — возвращает `bytea`
—

#### `public.pgp_sym_encrypt_bytea()` — возвращает `bytea`
—

#### `public.populate_record()` — возвращает `anyelement`
—

#### `public.skeys()` — возвращает `SETOF text`
—

#### `public.slice()` — возвращает `hstore`
—

#### `public.slice_array()` — возвращает `text[]`
—

#### `public.svals()` — возвращает `SETOF text`
—

#### `public.tconvert()` — возвращает `hstore`
—

#### `public.uuid_generate_v1()` — возвращает `uuid`
—

#### `public.uuid_generate_v1mc()` — возвращает `uuid`
—

#### `public.uuid_generate_v3()` — возвращает `uuid`
—

#### `public.uuid_generate_v4()` — возвращает `uuid`
—

#### `public.uuid_generate_v5()` — возвращает `uuid`
—

#### `public.uuid_nil()` — возвращает `uuid`
—

#### `public.uuid_ns_dns()` — возвращает `uuid`
—

#### `public.uuid_ns_oid()` — возвращает `uuid`
—

#### `public.uuid_ns_url()` — возвращает `uuid`
—

#### `public.uuid_ns_x500()` — возвращает `uuid`
—

---
## 📂 Схема: `users_schema`

### Таблицы схемы `users_schema`
| Таблица | Назначение |
|----------|-------------|
| global_attributes | — |
| user_global_attribute_assignments | — |
| users | — |

#### `users_schema.global_attributes`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| title | character varying | ✅ | — | — |
| description | text | ✅ | — | — |
| preferences_json | jsonb | ✅ | — | — |

#### `users_schema.user_global_attribute_assignments`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| user_id | bigint | ❌ | — | — |
| global_attribute_id | bigint | ❌ | — | — |
| assigned_at | timestamp without time zone | ✅ | — | — |

#### `users_schema.users`

| Поле | Тип | Nullable | Default | Описание |
|------|-----|-----------|----------|-----------|
| id | bigint | ❌ | — | — |
| login | character varying | ❌ | — | — |
| firstname | character varying | ✅ | — | — |
| lastname | character varying | ✅ | — | — |
| emails | ARRAY | ✅ | — | — |
| discord | character varying | ✅ | — | — |
| tg | character varying | ✅ | — | — |
| not_sending | boolean | ❌ | false | — |
| controlcenter_id | bigint | ✅ | — | — |
| avatar | bytea | ✅ | — | — |

### ⚙️ Функции схемы `users_schema`

#### `users_schema.assign_user_global_attribute()` — возвращает `boolean`
—

#### `users_schema.create_global_attribute_json()` — возвращает `jsonb`
—

#### `users_schema.create_user_json()` — возвращает `jsonb`
—

#### `users_schema.create_users_from_json()` — возвращает `None`
—

#### `users_schema.delete_global_attribute()` — возвращает `boolean`
—

#### `users_schema.delete_user()` — возвращает `boolean`
—

#### `users_schema.exists_global_attribute()` — возвращает `boolean`
—

#### `users_schema.exists_user()` — возвращает `boolean`
—

#### `users_schema.get_all_global_attributes_json()` — возвращает `jsonb`
—

#### `users_schema.get_all_users_json()` — возвращает `jsonb`
—

#### `users_schema.get_global_attribute_json()` — возвращает `jsonb`
—

#### `users_schema.get_global_attribute_user_ids_json()` — возвращает `jsonb`
—

#### `users_schema.get_global_attributes_with_users()` — возвращает `jsonb`
—

#### `users_schema.get_user_by_cc_json()` — возвращает `jsonb`
—

#### `users_schema.get_user_by_login_json()` — возвращает `jsonb`
—

#### `users_schema.get_user_global_attributes_json()` — возвращает `jsonb`
—

#### `users_schema.get_user_json()` — возвращает `jsonb`
—

#### `users_schema.is_user_global_attribute_assigned()` — возвращает `boolean`
—

#### `users_schema.sp_assign_team_attributes()` — возвращает `None`
—

#### `users_schema.unassign_user_global_attribute()` — возвращает `boolean`
—

#### `users_schema.update_global_attribute_json()` — возвращает `boolean`
—

#### `users_schema.update_user_json()` — возвращает `boolean`
—

#### `users_schema.user_row_to_json()` — возвращает `jsonb`
—

#### `users_schema.users_mute_simple()` — возвращает `void`
—

---