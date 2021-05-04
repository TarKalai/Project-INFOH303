"""
Sélectionnez le pays qui a administré le plus grand nombre total de vaccins (toutes les dates
cumulées);
"""
#With nbr_vacc_not_null (iso_code, nbr_vaccinations) as (SELECT iso_code, nbr_vaccinations
#                                                                    FROM Stat_Measures
#                                                                    where nbr_vaccinations > 0 )

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
            WITH TOT_VACC_BY_COUNTRY (iso_code, tot_vaccinations) AS (SELECT iso_code, SUM(nbr_vaccinations)
                                                            FROM Stat_Measures
                                                            WHERE nbr_vaccinations > 0 
                                                            GROUP BY iso_code)  
            
            SELECT iso_code, tot_vaccinations
            FROM TOT_VACC_BY_COUNTRY
			WHERE tot_vaccinations = (SELECT MAX(tot_vaccinations)
                                        FROM TOT_VACC_BY_COUNTRY)                 
            """)

rows = cur.fetchall()

for data in rows:
    print("iso_code : " + str(data[0]) + "                total number of vaccinations : " + str(data[1]))

print(len(rows))

print("Data selected Successfully")
conn.close()
