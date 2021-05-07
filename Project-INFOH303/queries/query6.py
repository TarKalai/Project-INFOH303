"""
Sélectionnez le nom des vaccins disponibles à la fois en Belgique et en France.
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
            SELECT cv1.vaccine_name
            FROM CountryVacc cv1, CountryVacc cv2
            WHERE cv1.vaccine_name = cv2.vaccine_name AND cv1.iso_code = 'BEL' AND cv2.iso_code = 'FRA'
            """)


rows = cur.fetchall()
for i in rows:
    print(i)
print(len(rows))

print("Data selected Successfully")
conn.close()