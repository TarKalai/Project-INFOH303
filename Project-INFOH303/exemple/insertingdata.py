import psycopg2

DB_NAME = "rdqxhttk"
DB_USER = "rdqxhttk"
DB_PASS = "iAs4oaszEn08NcQhuZNODLXpdqCid6yd"
DB_HOST = "hattie.db.elephantsql.com"
DB_PORT = "5432"


conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)


print("Database connected successfully")

cur = conn.cursor()

cur.execute("""INSERT INTO Employe (ID, NAME, EMAIL) VALUES (2, 'John', 'John@mail')""")
conn.commit()
print("Data inserted Successfully")
conn.close()
