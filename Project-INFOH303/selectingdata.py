import psycopg2

DB_NAME = "rdqxhttk"
DB_USER = "rdqxhttk"
DB_PASS = "iAs4oaszEn08NcQhuZNODLXpdqCid6yd"
DB_HOST = "hattie.db.elephantsql.com"
DB_PORT = "5432"


conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)


print("Database connected successfully")

cur = conn.cursor()

cur.execute("SELECT ID, NAME, EMAIL FROM Employe")

rows = cur.fetchall()

for data in rows:
    print("ID : " + str(data[0]))
    print("Name : " + data[1])
    print("Email : " + data[2])


print("Data selected Successfully")
conn.close()
