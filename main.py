# file: generate_filtered_schema_md.py
"""
Генератор Markdown-документации по структуре PostgreSQL (фильтр по схемам).
Извлекает таблицы, поля, функции и комментарии (включая комментарии к колонкам).
Схемы: policyregistry, users_schema, public.
"""

import psycopg2
from psycopg2 import sql
from pathlib import Path
from datetime import datetime

OUTPUT_FILE = Path("database_schema_filtered.md")

DB_CONFIG = {
    "host": "tech",
    "port": 5432,
    "dbname": "",
    "user": "",
    "password": "",
}

TARGET_SCHEMAS = ["audit", "migrations", "policyregistry", "public", "users_schema"]

SCHEMA_DESCRIPTIONS = {
    "audit": "Аудит",
    "migrations": "Миграции",
    "policyregistry": "Голосование",
    "public": "Общая",
    "users_schema": "Пользователи",
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


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


def generate_md():
    conn = get_connection()
    cur = conn.cursor()
    now = datetime.now().strftime("%d-%m-%Y")

    lines = [
        "# 🧩 Структура БД, включая схемы, таблицы и функции.",
        "",
        "**СУБД:** PostgreSQL",
        f"**Дата обновления:** {now}",
        "---",
    ]

    # --- Сводка по схемам ---
    schema_stats = {}
    for schema in TARGET_SCHEMAS:
        tables = get_tables(cur, schema)
        funcs = get_functions(cur, schema)
        schema_stats[schema] = {"tables": tables, "functions": funcs}

    lines.append("## 📂 Список схем\n")
    lines.append("| Схема | Таблиц | Функций | Назначение |")
    lines.append("|--------|---------|----------|----------|")

    for schema in TARGET_SCHEMAS:
        desc = SCHEMA_DESCRIPTIONS.get(schema, "")
        stats = schema_stats[schema]
        lines.append(f"| `{schema}` | {len(stats['tables'])} | {len(stats['functions'])} | {desc} |")

    lines.append("\n---")

    # --- Детализация схем ---
    for schema in TARGET_SCHEMAS:
        lines.append(f"## 📂 Схема: `{schema}`\n")

        tables = schema_stats[schema]["tables"]
        functions = schema_stats[schema]["functions"]

        # === Таблицы ===
        lines.append(f"### Таблицы схемы `{schema}`")
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
                lines.append(f"#### `{schema}.{table}`\n")
                lines.append("| Поле | Тип | Nullable | Default | Описание |")
                lines.append("|------|-----|-----------|----------|-----------|")
                for name, dtype, nullable, default, comment in cols:
                    lines.append(
                        f"| {name} | {dtype} | {'✅' if nullable == 'YES' else '❌'} | {default or '—'} | {comment or '—'} |"
                    )
                lines.append("")

        # === Функции ===
        lines.append(f"### ⚙️ Функции схемы `{schema}`\n")
        if not functions:
            lines.append("_(нет функций)_\n")
        else:
            for name, ret_type, comment in functions:
                desc = comment or "—"
                lines.append(f"#### `{schema}.{name}()` — возвращает `{ret_type}`")
                lines.append(f"{desc}\n")

        lines.append("---")

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    cur.close()
    conn.close()
    print(f"✅ Markdown-схема успешно сгенерирована: {OUTPUT_FILE.absolute()}")


if __name__ == "__main__":
    generate_md()
