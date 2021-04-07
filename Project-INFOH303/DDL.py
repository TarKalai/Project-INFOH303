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
iso_code VARCHAR (3) PRIMARY KEY,
continent TEXT NOT NULL,
region TEXT NOT NULL,
name TEXT NOT NULL,
hdi FLOAT,
population INT NOT NULL,
area_sq_ml INT NOT NULL,
climate_id INT
)

CREATE TABLE Climate (
id INT PRIMARY KEY,
description TEXT NOT NULL,
)

CREATE TABLE Cure (
c_iso_code VARCHAR (3) PRIMARY KEY,
date DATE NOT NULL,
)

CREATE TABLE CureVacc ( neeeddddd toooo reworrrk "two KEY"
c_iso_code VARCHAR (3) PRIMARY KEY,
vaccines TEXT NOT NULL,
)

""")

conn.commit()

print("Table created successfully")
conn.close()