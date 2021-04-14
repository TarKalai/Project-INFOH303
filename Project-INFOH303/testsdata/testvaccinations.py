import csv


producersFile = "D:\\documents\\BA3 Polytechnique\\INFO-H303\\Projet_partie_2\\Project-INFOH303\\data_csv_files\\vaccinations.csv"
#mettre un path absolu

def open_folder_csv(file, list):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            list.append(line)



def start_project():
    list_of_producers = []
    open_folder_csv(producersFile, list_of_producers)
    for i in range(len(list_of_producers)-1):
        if list_of_producers[i + 1][2] != "" and int(float(list_of_producers[i + 1][2])) >2147483647:
            print(int(float(list_of_producers[i + 1][2])))
        #else:
            #print(list_of_producers[i + 1][1])



start_project()

"""



"""
