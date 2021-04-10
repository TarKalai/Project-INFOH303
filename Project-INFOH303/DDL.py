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
         
CREATE TABLE Country (
iso_code CHAR (3) PRIMARY KEY,
continent VARCHAR (16) NOT NULL,
region VARCHAR (24) NOT NULL,
name VARCHAR (36) NOT NULL,
hdi DECIMAL(1,3) NOT NULL,
population INT NOT NULL,
area_sq_ml INT NOT NULL,
first_vaccination_date DATE,
climate_id TINYINT
);

CREATE TABLE Climate (
id TINYINT PRIMARY KEY,
description VARCHAR (100) NOT NULL
);

CREATE TABLE CountryVacc (
iso_code CHAR (3) NOT NULL,
vaccine_name VARCHAR (22) NOT NULL,
CONSTRAINT CompKey_code_name PRIMARY KEY (iso_code,vaccine_name)
);

CREATE TABLE Stat_Hospitalisation (
id INT PRIMARY KEY,
date DATE NOT NULL,
icu_patients INT NOT NULL,
hosp_patients INT NOT NULL,
epidemiologist_source CHAR (36) NOT NULL
);


""")

conn.commit()

print("Table created successfully")
conn.close()