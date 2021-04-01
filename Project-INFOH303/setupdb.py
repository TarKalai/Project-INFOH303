import psycopg2

DB_NAME = "rdqxhttk"
DB_USER = "rdqxhttk"
DB_PASS = "iAs4oaszEn08NcQhuZNODLXpdqCid6yd"
DB_HOST = "hattie.db.elephantsql.com"
DB_PORT = "5432"


conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)


print("Database connected successfully")

cur = conn.cursor()
cur.execute("""

CREATE TABLE climate (
id INT PRIMARY KEY,
description TEXT NOT NULL,
)

CREATE TABLE hospitalizations (
id INT PRIMARY KEY,
description TEXT NOT NULL,
)

iso_code,date,icu_patients,hosp_patients,source_epidemiologiste
""")

conn.commit()

print("Table created successfully")
conn.close()