import os
import psycopg2
from psycopg2 import sql
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv


# Загрузить переменные окружения из .env (если файл существует)
load_dotenv()

OUTPUT_FILE = Path("database.md")

DEFAULT_PROD_SCHEMAS = [
    "audit", 
    "cron", 
    "meritfund", 
    "migrations", 
    "policyregistry", 
    "users_schema"
]

DEFAULT_STAGE_SCHEMAS = []

SCHEMA_DESCRIPTIONS = {
    "audit": "Аудит",
    "cron": "Планировщик",
    "meritfund": "Меритфонд",
    "migrations": "Миграции",
    "policyregistry": "Трибуна",
    "public": "Общая (Для DevOps-сов)",
    "users_schema": "Пользователи",
}


def parse_csv_env(name, default=None):
    value = os.getenv(name)
    if not value:
        return list(default or [])
    return [item.strip() for item in value.split(",") if item.strip()]


def get_db_config(prefix, fallback_to_plain=False):
    def env_value(key, default=""):
        prefixed = os.getenv(f"{prefix}_{key}")
        if prefixed is not None:
            return prefixed
        if fallback_to_plain:
            return os.getenv(key, default)
        return default

    return {
        "host": env_value("DB_HOST"),
        "port": int(env_value("DB_PORT", 5432)),
        "dbname": env_value("DB_NAME"),
        "user": env_value("DB_USER"),
        "password": env_value("DB_PASSWORD"),
    }


ENVIRONMENTS = [
    {
        "name": "prod",
        "title": "Production",
        "db_config": get_db_config("PROD", fallback_to_plain=True),
        "schemas": parse_csv_env("PROD_DB_SCHEMAS", DEFAULT_PROD_SCHEMAS),
    },
    {
        "name": "stage",
        "title": "Stage",
        "db_config": get_db_config("STAGE"),
        "schemas": parse_csv_env("STAGE_DB_SCHEMAS", DEFAULT_STAGE_SCHEMAS),
    },
]


def is_environment_configured(environment):
    config = environment["db_config"]
    return all(config[key] for key in ("host", "dbname", "user", "password")) and bool(environment["schemas"])


def get_connection(db_config):
    return psycopg2.connect(**db_config)


def get_tables(cur, schema):
    cur.execute(
        sql.SQL("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = %s
            ORDER BY table_name;
        """),
        [schema],
    )
    return [r[0] for r in cur.fetchall()]


def get_table_comment(cur, schema, table):
    cur.execute(
        sql.SQL("""
            SELECT obj_description((quote_ident(%s)||'.'||quote_ident(%s))::regclass, 'pg_class');
        """),
        [schema, table],
    )
    row = cur.fetchone()
    return row[0] if row and row[0] else ""


def get_columns_with_comments(cur, schema, table):
    """Возвращает колонки и комментарии к ним"""
    cur.execute(
        sql.SQL("""
            SELECT
                c.column_name,
                c.data_type,
                c.is_nullable,
                c.column_default,
                pgd.description
            FROM information_schema.columns c
            LEFT JOIN pg_catalog.pg_description pgd
                ON pgd.objsubid = c.ordinal_position
                AND pgd.objoid = (quote_ident(c.table_schema)||'.'||quote_ident(c.table_name))::regclass
            WHERE c.table_schema = %s AND c.table_name = %s
            ORDER BY c.ordinal_position;
        """),
        [schema, table],
    )
    return cur.fetchall()


def get_functions(cur, schema):
    cur.execute(
        sql.SQL("""
            SELECT p.proname AS func_name,
                   pg_catalog.pg_get_function_result(p.oid) AS return_type,
                   d.description
            FROM pg_proc p
            JOIN pg_namespace n ON n.oid = p.pronamespace
            LEFT JOIN pg_description d ON d.objoid = p.oid
            WHERE n.nspname = %s
            ORDER BY p.proname;
        """),
        [schema],
    )
    return cur.fetchall()


def build_intro_lines(now):
    return [
        "# 🧩 Структура БД на prod и stage окружениях: схемы, таблицы и функции.",
        "",
        "**СУБД:** PostgreSQL",
        f"**Дата обновления:** {now}",
        "",
        "---",
        "",
        "## 📚 Аудит голосований",
        "",
        "- [Информация по аудиту](vote-sessions-audit.md)",
        "",
        "---",
        "",
        "## 🗄️ Файлы миграций схем",
        "",
        "- [audit](migrations/audit)",
        "- [meritfund](migrations/meritfund)",
        "- [policyregistry](migrations/policyregistry)",
        "",
        "---",
        "",
        "## ⏱️ Планировщик",
        "",
        "- [Cron-задания](crone-database.md)",
        "",
        "---",
    ]


def generate_environment_md(environment):
    conn = get_connection(environment["db_config"])
    try:
        cur = conn.cursor()
        target_schemas = environment["schemas"]
        lines = [
            f"## Окружение: {environment['title']} (`{environment['name']}`)",
            "",
        ]

        schema_stats = {}
        for schema in target_schemas:
            tables = get_tables(cur, schema)
            funcs = get_functions(cur, schema)
            schema_stats[schema] = {"tables": tables, "functions": funcs}

        lines.append("### 📂 Список схем\n")
        lines.append("| Схема | Таблиц | Функций | Назначение |")
        lines.append("|--------|---------|----------|----------|")

        for schema in target_schemas:
            desc = SCHEMA_DESCRIPTIONS.get(schema, "")
            stats = schema_stats[schema]
            lines.append(f"| `{schema}` | {len(stats['tables'])} | {len(stats['functions'])} | {desc} |")

        lines.append("\n---")

        # --- Детализация схем ---
        for schema in target_schemas:
            lines.append(f"### 📂 Схема: `{schema}`\n")

            tables = schema_stats[schema]["tables"]
            functions = schema_stats[schema]["functions"]

            # === Таблицы ===
            lines.append(f"#### Таблицы схемы `{schema}`")
            if not tables:
                lines.append("_(нет таблиц)_\n")
            else:
                lines.append("| Таблица | Назначение |")
                lines.append("|----------|-------------|")
                for table in tables:
                    comment = get_table_comment(cur, schema, table) or "—"
                    lines.append(f"| {table} | {comment} |")
                lines.append("")

                for table in tables:
                    cols = get_columns_with_comments(cur, schema, table)
                    lines.append(f"##### `{schema}.{table}`\n")
                    lines.append("| Поле | Тип | Nullable | Default | Описание |")
                    lines.append("|------|-----|-----------|----------|-----------|")
                    for name, dtype, nullable, default, comment in cols:
                        lines.append(
                            f"| {name} | {dtype} | {'✅' if nullable == 'YES' else '❌'} | {default or '—'} | {comment or '—'} |"
                        )
                    lines.append("")

            # === Функции ===
            lines.append(f"#### ⚙️ Функции схемы `{schema}`\n")
            if not functions:
                lines.append("_(нет функций)_\n")
            else:
                for name, ret_type, comment in functions:
                    desc = comment or "—"
                    lines.append(f"##### `{schema}.{name}()` — возвращает `{ret_type}`")
                    lines.append(f"{desc}\n")

            lines.append("---")

        cur.close()
        return lines
    finally:
        conn.close()


def build_common_reference_lines():
    return [
        "",
        "## 📋 Регламент ",
        "",
        "- [Работа с базами данных](https://git.imbalanced.tech/government/agreements-policies-regulations/-/blob/main/guidelines/%D0%A0%D0%B5%D0%B3%D0%BB%D0%B0%D0%BC%D0%B5%D0%BD%D1%82_%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8_%D0%91%D0%94.md)",
        "- Именование сущностей баз данных (в разработке)",
        "",
        "---",
        "",
        "## 🖥️ Мониторинг производительности ",
        "",
        "- [pgBadger](monitor/pgbadger.md)",
        "- [pgStatStatements](monitor/pgstatstatements.md)",
        "",
        "---",
        "",
        "## 🗄️ Резервное копирование ",
        "",
        "- [pgBackWeb](backup/pgbackweb.md)",
        "",
        "---",
    ]


def generate_md():
    now = datetime.now().strftime("%d-%m-%Y")
    lines = build_intro_lines(now)
    configured_environments = [env for env in ENVIRONMENTS if is_environment_configured(env)]

    if not configured_environments:
        raise RuntimeError(
            "Не настроено ни одно окружение. Проверьте DB_* для prod или STAGE_DB_* и STAGE_DB_SCHEMAS для stage."
        )

    for environment in configured_environments:
        lines.extend(generate_environment_md(environment))

    lines.extend(build_common_reference_lines())

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ Markdown-схема успешно сгенерирована: {OUTPUT_FILE.absolute()}")


if __name__ == "__main__":
    generate_md()
