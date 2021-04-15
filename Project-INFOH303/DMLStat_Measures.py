import psycopg2
import csv
import os
print(os.path.abspath(os.curdir))
StatMeasuresFile = os.path.abspath(os.curdir) + "\\data_csv_files\\vaccinations.csv"
CountryFile = os.path.abspath(os.curdir) + "\\data_csv_files\\country.csv"
# mettre un path absolu

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
a = 0
for i in list_of_Vacc:
    if i[0] in list_cut:
        list_temp.append([i[0], isolate_date(i[1]), convert_to_int(i[2]), convert_to_int(i[3])])
        a += 1
    else:
        print(i)
print(len(list_of_Vacc)-a)


tuples = tuple(tuple(x) for x in list_temp)

#print(tuples)

