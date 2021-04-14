import csv
import pkg_resources

path = "data_csv_files/country.csv"
hospitalsFile = "D:\\documents\\BA3 Polytechnique\\INFO-H303\\Projet_partie_2\\Project-INFOH303\\data_csv_files\\hospitals.csv"
#mettre un path absolu

def open_folder_csv(file, list):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            list.append(line)



def start_project():
    list_of_country = []
    open_folder_csv(hospitalsFile, list_of_country)
    for i in range(len(list_of_country)-1):
        if len(list_of_country[i + 1][4]) != 36:
            print("Huston, we have a problem")
        else:
            print(len(list_of_country[i+1][4]))



start_project()

"""
pour coutry : 
filtrage pour la colonne icu_patiens (colonne 2, transformer les floats en ints)
filtrage pour la colonne hosp_patiens (colonne 3, transformer les floats en ints)
filtrage pour la ligne hdi : round(float(list_of_country[i+1][4]), 3)


"""
