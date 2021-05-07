"""
La proportion de la population hospitalisée pour chaque pays, le 1er janvier 2021;
"""

import psycopg2

DB_NAME = "INFO-H303"
DB_USER = "postgres"
DB_PASS = "root"
DB_HOST = "localhost"
DB_PORT = "5432"

"""
DB_NAME = "rdqxhttk"
DB_USER = "rdqxhttk"
DB_PASS = "iAs4oaszEn08NcQhuZNODLXpdqCid6yd"
DB_HOST = "hattie.db.elephantsql.com"
DB_PORT = "5432"
"""

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database connected successfully")

cur = conn.cursor()

cur.execute("""    
            WITH S (date, iso_code, hosp_patients) AS (SELECT date, iso_code, hosp_patients
                                                       FROM Stat_Hospitalization),
	             C (name, iso_code, population) AS (SELECT name, iso_code, population
                                                    FROM Country)
            SELECT c.name, CONCAT(ROUND(CAST(CAST(sh.hosp_patients*100 AS FLOAT)/CAST(c.population AS FLOAT) AS NUMERIC), 4), ' %')
            FROM C c, S sh
            WHERE c.iso_code = sh.iso_code AND sh.date = '2021-01-01'
            """)


rows = cur.fetchall()
for i in rows:
    print(i)
print(len(rows))

print("Data selected Successfully")
conn.close()