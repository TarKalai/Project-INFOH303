import psycopg2
import csv
import os
print(os.path.abspath(os.curdir))
epidemologistFile = os.path.abspath(os.curdir) + "\\data_csv_files\\hospitals.csv"

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
    if number != '' or number != '0.0':
        a = int(float(number))
    else:
        print("j'étais vide")
    return a

def convert_to_date(date):
    temp_date = ""
    temp_date += date[6]
    temp_date += date[7]
    temp_date += date[8]
    temp_date += date[9]
    temp_date += "-"
    temp_date += date[3]
    temp_date += date[4]
    temp_date += "-"
    temp_date += date[0]
    temp_date += date[1]
    return temp_date

open_folder_csv(epidemologistFile, list_of_epidemiologist, ',')


# Retire le premier élément de la liste (titre des données)
list_of_epidemiologist.pop(0)

id = 1
for i in list_of_epidemiologist:
    date = convert_to_date(i[1])
    iso_code = i[0]
    icu_patients = convert_to_int(i[2])
    hosp_patients = convert_to_int(i[3])
    epidemiologist_source = i[4]
    list_temp.append([id, date, icu_patients, hosp_patients, epidemiologist_source, iso_code])
    id += 1


tuples = tuple(tuple(x) for x in list_temp)
#print(tuples)

for i in list_temp:
    if i[3] > 32000:
        print("tu devras etre un int")


DB_NAME = "rdqxhttk"
DB_USER = "rdqxhttk"
DB_PASS = "iAs4oaszEn08NcQhuZNODLXpdqCid6yd"
DB_HOST = "hattie.db.elephantsql.com"
DB_PORT = "5432"

con = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database connected successfully")

with con:
    cur = con.cursor()
    query = "INSERT INTO Stat_Hospitalization (id, date, icu_patients, hosp_patients, epidemiologist_source, iso_code) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.executemany(query, tuples)
    con.commit()

print("Data inserted Successfully")
con.close()



