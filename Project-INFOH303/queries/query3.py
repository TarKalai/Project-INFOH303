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
            WITH vacc_name (vaccine_name) as (SELECT vaccine_name
                                                FROM CountryVacc 
                                                group by vaccine_name
                                                order by vaccine_name)
            SELECT vaccine_name, ARRAY (SELECT c.name
                                        FROM CountryVacc cv, Country c
                                        WHERE cv.vaccine_name = vn.vaccine_name and c.iso_code = cv.iso_code)
            FROM vacc_name vn                

            """)


rows = cur.fetchall()
for i in rows:
    print(i)

print("Data selected Successfully")
conn.close()