import csv
import psycopg2

DB_NAME = "rdqxhttk"
DB_USER = "rdqxhttk"
DB_PASS = "iAs4oaszEn08NcQhuZNODLXpdqCid6yd"
DB_HOST = "hattie.db.elephantsql.com"
DB_PORT = "5432"

climateFile = "data_csv_files/climate.csv"
countryFile = "data_csv_files/country.csv"


def open_folder_csv(file, list):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for line in csv_reader:
            list.append(line)


def connect_to_db():
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        print("Database connected successfully")
        return conn
    except:
        print("An error has occured while trying to connect to the database.")


def isolate_name_of_file(filename):
    name_of_table = ""
    a = 0
    b = 0
    for i in range(len(filename)):
        if filename[i] == '/':
            a = i + 1
        elif filename[i] == '.':
            b = i
    name_of_table = filename[a:b]
    return name_of_table


def start_project():
    list_of_country = []
    open_folder_csv(countryFile, list_of_country)




start_project()


