import psycopg2
import csv

path = "data_csv_files/country.csv"
countryFile = "D:\\documents\\BA3 Polytechnique\\INFO-H303\\Projet_partie_2\\Project-INFOH303\\data_csv_files\\country.csv"
# mettre un path absolu
list_of_country = []


def open_folder_csv(file, list):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for line in csv_reader:
            list.append(line)


open_folder_csv(countryFile, list_of_country)

list_of_country.pop(0)

for i in range(len(list_of_country)):
    #transformation de "hdi" en float arrondi a 3 chiffre apres la virgule
    list_of_country[i][4] = round(float(list_of_country[i][4]), 3)
    #transformation de climat_id en int s'il existe, none sinon
    if list_of_country[i][7] == "":
        list_of_country[i][7] = None
    else:
        list_of_country[i][7] = int(list_of_country[i][7])
    #transformation de population en int
    list_of_country[i][5] = int(list_of_country[i][5])
    #transformation de area_sq_ml
    list_of_country[i][6] = int(list_of_country[i][6])


tuples = tuple(tuple(x) for x in list_of_country)

print(tuples)


DB_NAME = "rdqxhttk"
DB_USER = "rdqxhttk"
DB_PASS = "iAs4oaszEn08NcQhuZNODLXpdqCid6yd"
DB_HOST = "hattie.db.elephantsql.com"
DB_PORT = "5432"

con = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database connected successfully")

with con:
    cur = con.cursor()
    query = "INSERT INTO Country (iso_code, continent ,region, name, hdi, population, area_sq_ml, climate_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
    cur.executemany(query, tuples)
    con.commit()

print("Data inserted Successfully")
con.close()
