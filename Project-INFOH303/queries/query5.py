"""
Calculez l’évolution, pour chaque jour et chaque pays, du nombre de patients hospitalisés
(hosp_patients);
Vous devez pour cette requête calculer la différence, pour chaque jour et chaque pays, entre la
valeur de hosp_patients et sa valeur le jour précédent. Par exemple, pour l’Autriche, vous
aurez quelque chose comme:
20/01/2021 -46
21/01/2021 -77
22/01/2021 -20
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
            WITH SH1 (iso_code, date, hosp_patients) AS (SELECT iso_code, date, hosp_patients
                                                         FROM Stat_Hospitalization), 
                 SH2 (iso_code, date, hosp_patients) AS (SELECT *
                                                         FROM SH1)       
            SELECT sh2.iso_code, CAST(sh2.date AS VARCHAR), sh2.hosp_patients - sh1.hosp_patients
            FROM SH1 sh1, SH2 sh2
            WHERE sh1.date = sh2.date-1 AND sh1.iso_code = sh2.iso_code
            ORDER BY iso_code, date
            """)


rows = cur.fetchall()
for i in rows:
    print(i)
print(len(rows))

print("Data selected Successfully")
conn.close()