import csv
import pkg_resources
import os
path = "data_csv_files/country.csv"
climateFile = os.path.abspath(os.curdir) + "data_csv_files\\climate.csv"


def open_folder_csv(file, list):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for line in csv_reader:
            list.append(line)



def start_project():
    list_of_country = []
    open_folder_csv(climateFile, list_of_country)
    for i in range(len(list_of_country)-1):
        if list_of_country[i + 1][1] == "":
            print("Bonjour il y a un probleme")
        else:
            print(len(list_of_country[i+1][1]))



start_project()

"""
pour coutry : 
filtrage pour la ligne climat : if list_of_country[i+1][7] == "":print("null")
filtrage pour la ligne hdi : round(float(list_of_country[i+1][4]), 3)


"""
