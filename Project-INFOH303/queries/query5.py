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

DB_NAME = "rdqxhttk"
DB_USER = "rdqxhttk"
DB_PASS = "iAs4oaszEn08NcQhuZNODLXpdqCid6yd"
DB_HOST = "hattie.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database connected successfully")

cur = conn.cursor()

cur.execute("""        
            SELECT sh2.iso_code, cast(sh2.date as varchar), sh2.hosp_patients - sh1.hosp_patients
            FROM Stat_Hospitalization sh1, Stat_Hospitalization sh2
            WHERE sh1.date = sh2.date-1 and sh1.iso_code = sh2.iso_code
            """)


rows = cur.fetchall()
for i in rows:
    print(i)
print(len(rows))

print("Data selected Successfully")
conn.close()