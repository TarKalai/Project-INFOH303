""""
Sélectionnez les pays qui, au même moment, ont eu au moins 5000 personnes hospitalisées
(hosp_patients);
Chaque pays doit apparaître une seule fois au maximum dans le résultat de votre requête.
"""


# version avec comparaison entre pays
#With
#stat5000(iso_code, date) as (SELECT iso_code, date
#FROM Stat_hospitalization
#WHERE hosp_patients >= 5000)
#
#SELECT
#DISTINCT
#s1.iso_code
#FROM
#stat5000
#s1, stat5000
#s2
#WHERE
#s1.date = s2.date and s1.iso_code <> s2.iso_code

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
            SELECT iso_code
            FROM Stat_hospitalization 
            WHERE hosp_patients >= 5000
            GROUP BY iso_code                       
            """)

rows = cur.fetchall()

for data in rows:
    print("iso_code : " + str(data[0]))

print(len(rows))


print("Data selected Successfully")
conn.close()