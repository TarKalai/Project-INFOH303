import psycopg2

DB_NAME = "INFO-H303"
DB_USER = "postgres"
DB_PASS = "root"
DB_HOST = "localhost"
DB_PORT = "5432"


conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database connected successfully")

cur = conn.cursor()
cur.execute("""

CREATE TABLE Climate (
id SMALLINT PRIMARY KEY,
description VARCHAR (100) NOT NULL
);


CREATE TABLE Country (
iso_code CHAR (3) PRIMARY KEY,
continent VARCHAR (16) NOT NULL,
region VARCHAR (24) NOT NULL,
name VARCHAR (36) NOT NULL,
hdi NUMERIC(3,3) NOT NULL,
population INT NOT NULL,
area_sq_ml INT NOT NULL,
first_vaccination_date DATE,
climate_id SMALLINT,
CONSTRAINT fk_climate_id FOREIGN KEY (climate_id) REFERENCES Climate(id)
);

CREATE TABLE CountryVacc (
iso_code CHAR (3) NOT NULL,
vaccine_name VARCHAR (22) NOT NULL,
CONSTRAINT CompKey_code_name PRIMARY KEY (iso_code,vaccine_name),
CONSTRAINT fk_iso_code FOREIGN KEY (iso_code) REFERENCES Country(iso_code)
);


CREATE TABLE Stat_Measures(
id INT PRIMARY KEY,
date DATE NOT NULL,
tests INT,
nbr_vaccinations INT,
iso_code CHAR (3) NOT NULL,
CONSTRAINT fk_iso_code FOREIGN KEY (iso_code) REFERENCES Country(iso_code)
);

CREATE TABLE People(
user_source CHAR (36) PRIMARY KEY,
username VARCHAR NOT NULL ,
lastname VARCHAR NOT NULL,
firstname VARCHAR NOT NULL,
adress VARCHAR NOT NULL,
password VARCHAR NOT NULL
);

CREATE TABLE Epidemiologist(
epidemiologist_source CHAR (36) PRIMARY KEY,
CONSTRAINT fk_epidemiologist_source FOREIGN KEY (epidemiologist_source) REFERENCES People(user_source),
center VARCHAR,
service_phone VARCHAR
) INHERITS (People);

CREATE TABLE Stat_Hospitalization (
id SMALLINT PRIMARY KEY,
date DATE NOT NULL,
icu_patients INT NOT NULL,
hosp_patients INT NOT NULL,
epidemiologist_source CHAR (36) NOT NULL,
CONSTRAINT fk_epidemiologist_source FOREIGN KEY (epidemiologist_source) REFERENCES Epidemiologist(epidemiologist_source),
iso_code CHAR (3) NOT NULL,
CONSTRAINT fk_iso_code FOREIGN KEY (iso_code) REFERENCES Country(iso_code)
);



""")

conn.commit()

print("Tables created successfully")
conn.close()