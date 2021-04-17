import psycopg2
import csv

path = "../data_csv_files/country.csv"
countryVaccFile = "C:\\Users\\takira\\Desktop\\ULB\\BA3-IRCI\\Q2\\Bases de données INFO-H303\\Projet\\Partie_2\\Project-INFOH303\\Project-INFOH303\\data_csv_files\\producers.csv"
# mettre un path absolu

list_of_Vacc = []

list_temp = []


def open_folder_csv(file, list):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for line in csv_reader:
            list.append(line)


open_folder_csv(countryVaccFile, list_of_Vacc)

#Retire le premier élément de la liste (titre des données)
list_of_Vacc.pop(0)

#Création d'une liste temporaire pour garder les 2 éléments intéressants
for i in range(len(list_of_Vacc)):
    x = list_of_Vacc[i][2].split(", ")
    for j in x :
        list_temp.append([list_of_Vacc[i][0], j])



tuples = tuple(tuple(x) for x in list_temp)

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
    query = "INSERT INTO CountryVacc (iso_code, vaccine_name) VALUES (%s, %s)"
    cur.executemany(query, tuples)
    con.commit()

print("Data inserted Successfully")
con.close()
