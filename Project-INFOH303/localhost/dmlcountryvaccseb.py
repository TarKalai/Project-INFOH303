import psycopg2
import csv
import os
from pathlib import Path
path = Path(os.path.abspath(os.curdir)).parent.absolute()

countryVaccFile = str(path) + '/data_csv_files/producers.csv'
countryFile = str(path) + '/data_csv_files/country.csv'

list_of_Vacc = []
list_of_country = []
list_of_iso = []
list_temp = []


def open_folder_csv(file, list):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for line in csv_reader:
            list.append(line)


open_folder_csv(countryVaccFile, list_of_Vacc)
open_folder_csv(countryFile, list_of_country)

#Retire le premier élément de la liste (titre des données)
list_of_Vacc.pop(0)
list_of_country.pop(0)

#Création d'une liste temporaire pour garder les 2 éléments intéressants
for i in range(len(list_of_country)):
    list_of_iso.append(list_of_country[i][0])


for i in range(len(list_of_Vacc)):
    if list_of_Vacc[i][0] in list_of_iso:
        x = list_of_Vacc[i][2].split(", ")
        for j in x:
            list_temp.append([list_of_Vacc[i][0], j])



tuples = tuple(tuple(x) for x in list_temp)

print(tuples)


DB_NAME = "INFO-H303"
DB_USER = "postgres"
DB_PASS = "root"
DB_HOST = "localhost"
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
