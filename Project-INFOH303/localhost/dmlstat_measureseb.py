import psycopg2
import csv
import os
from pathlib import Path

path = Path(os.path.abspath(os.curdir)).parent.absolute()
StatMeasuresFile = str(path) + "/data_csv_files/vaccinations.csv"
CountryFile = str(path) + "/data_csv_files/country.csv"

list_of_Vacc = []
list_of_countries = []
list_temp = []
list_cut = []


def open_folder_csv(file, list, delim):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delim)
        for line in csv_reader:
            list.append(line)

def isolate_date(date):
    name_of_table = ""
    b = 0
    for i in range(len(date)):
        if date[i] == ' ':
            b = i
    name_of_table = date[0:b]
    return name_of_table

def convert_to_int(number):
    a = None
    if number != '':
        a = int(float(number))
    return a

open_folder_csv(StatMeasuresFile, list_of_Vacc, ',')
open_folder_csv(CountryFile, list_of_countries, ';')

#Retire le premier élément de la liste (titre des données)
list_of_Vacc.pop(0)
list_of_countries.pop(0)


for e in list_of_countries:
    list_cut.append(e[0])

id = 1
for i in list_of_Vacc:
    if i[0] in list_cut: #filtrage des iso_code qui ne sont pas dans country
        tests = convert_to_int(i[2])
        nbr_vaccinations = convert_to_int(i[3])
        if tests is not None or nbr_vaccinations is not None:  # filtrage des valeur ou les deux sont null
            iso_code = i[0]
            date = isolate_date(i[1])
            list_temp.append([id, date, tests, nbr_vaccinations, iso_code])
            id += 1


tuples = tuple(tuple(x) for x in list_temp)
print(len(list_temp))

DB_NAME = "INFO-H303"
DB_USER = "postgres"
DB_PASS = "root"
DB_HOST = "localhost"
DB_PORT = "5432"

con = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database connected successfully")

with con:
    cur = con.cursor()
    query = "INSERT INTO Stat_Measures (id, date, tests, nbr_vaccinations, iso_code) VALUES (%s, %s, %s, %s, %s)"
    cur.executemany(query, tuples)
    con.commit()

print("Data inserted Successfully")
con.close()

#print(tuples)

