"""
Pour chaque vaccin, sélectionnez le nom des pays qui l’utilisent.
Idéalement, vous pouvez essayer de retourner la liste des pays sous forme d’array. Vous
obtiendrez quelque chose comme:
(‘CNBG’, [‘China’])
(‘Moderna’, [‘Belgium’, ‘Bulgaria’, ‘Canada’, …])
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
            WITH VACC_NAME (vaccine_name) AS (SELECT vaccine_name
                                                FROM CountryVacc 
                                                GROUP BY vaccine_name
                                                ORDER BY vaccine_name),
                 C (name, iso_code) AS (SELECT name, iso_code
                                        FROM Country)
                                        
            SELECT vaccine_name, ARRAY (SELECT c.name
                                        FROM CountryVacc cv, C c
                                        WHERE cv.vaccine_name = vn.vaccine_name AND c.iso_code = cv.iso_code
                                        ORDER BY name)
            FROM VACC_NAME vn                

            """)


rows = cur.fetchall()
for i in rows:
    print(i)

print("Data selected Successfully")
conn.close()