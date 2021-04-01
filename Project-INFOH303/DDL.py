import csv

climateFile = "data_csv_files/climate.csv"


def open_folder_csv(file, list):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for line in csv_reader:
            list.append(line)


def start_project():
    list_of_climates = []
    open_folder_csv(climateFile, list_of_climates)
    print(list_of_climates)


start_project()
