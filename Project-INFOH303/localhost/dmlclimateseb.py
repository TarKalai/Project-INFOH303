import psycopg2
import csv
import os
from pathlib import Path
path = Path(os.path.abspath(os.curdir)).parent.absolute()
str_path = str(path) + '/data_csv_files/climate.csv'
climateFile = str_path
list_of_climate = []


def open_folder_csv(file, list):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for line in csv_reader:
            list.append(line)


open_folder_csv(climateFile, list_of_climate)

list_of_climate.pop(0)

for i in range(len(list_of_climate)):
    list_of_climate[i][0] = int(list_of_climate[i][0])

lst = [[1, 2], [3, 4], [5, 6]]
tuples = tuple(tuple(x) for x in list_of_climate)
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
    query = "INSERT INTO Climate (id, description) VALUES (%s, %s)"
    cur.executemany(query, tuples)
    con.commit()

print("Data inserted Successfully")
con.close()
