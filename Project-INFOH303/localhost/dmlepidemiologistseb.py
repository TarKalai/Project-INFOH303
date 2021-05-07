import psycopg2
import csv
import os
from pathlib import Path

path = Path(os.path.abspath(os.curdir)).parent.absolute()
epidemologistFile = str(path) + "/data_csv_files/hospitals.csv"

list_of_epidemiologist = []
list_temp = []


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


open_folder_csv(epidemologistFile, list_of_epidemiologist, ',')

# Retire le premier élément de la liste (titre des données)
list_of_epidemiologist.pop(0)

for i in list_of_epidemiologist:
    if [i[-1], i[-1]] not in list_temp:
        list_temp.append([i[-1], i[-1]])

print(list_temp)
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
    query = "INSERT INTO Epidemiologist (user_source, epidemiologist_source) VALUES (%s, %s)"
    cur.executemany(query, tuples)
    con.commit()

print("Data inserted Successfully")
con.close()
