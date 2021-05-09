import psycopg2


DB_NAME = "INFO-H303"
DB_USER = "postgres"
DB_PASS = "root"
DB_HOST = "localhost"
DB_PORT = "5432"


def firstQuery():
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


def secondQuery():
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


def thirdQuery():
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
    print(len(rows))
    print("Data selected Successfully")
    conn.close()


def fourthQuery():
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


def fifthQuery():
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


def sixthQuery():
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
