import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")

if not os.path.exists(DB_PATH):
    raise FileNotFoundError(f"No encuentro la base en: {DB_PATH}")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# 1) Buscar todas las tablas que empiezan con mensajeria_
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'mensajeria_%';")
tablas = [row[0] for row in cur.fetchall()]

# 2) Borrarlas
for t in tablas:
    cur.execute(f"DROP TABLE IF EXISTS {t};")

# 3) Borrar migraciones SOLO de la app mensajeria
cur.execute("DELETE FROM django_migrations WHERE app = 'mensajeria';")

conn.commit()
conn.close()

print("✅ OK: borré TODAS las tablas mensajeria_* y reinicié migraciones de mensajeria.")
