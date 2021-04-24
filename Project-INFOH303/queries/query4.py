"""
La proportion de la population hospitalisée pour chaque pays, le 1er janvier 2021;
"""

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
            SELECT c.name, CONCAT(round(cast(cast(sh.hosp_patients*100 as float)/cast(c.population as float) as numeric),4),' %')
            FROM Country c, Stat_Hospitalization sh
            WHERE c.iso_code = sh.iso_code and sh.date = '2021-01-01'
            """)


rows = cur.fetchall()
for i in rows:
    print(i)
print(len(rows))

print("Data selected Successfully")
conn.close()