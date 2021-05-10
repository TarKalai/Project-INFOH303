from tkinter import *
import psycopg2
import UserInterface as us
import EpidemiologistInterface as ep

DB_NAME = "INFO-H303"
DB_USER = "postgres"
DB_PASS = "root"
DB_HOST = "localhost"
DB_PORT = "5432"

# Initialise Connection Page
root = Tk()
root.title("Base de données Covid - Visiteur")
root.geometry("300x200")
myLabelUser = Label(root, text="Username : ")
myLabelPassword = Label(root, text="Password : ")
EntryUser = Entry(root)
EntryPassword = Entry(root, show="*")


def controlLogIn():
    """
    Vérifie le type d'utilisateur dans l'application pour aller à la bonne page suivante
    :return: void
    """
    username = EntryUser.get()
    password = EntryPassword.get()
    people = getPeople()
    epidemiologist = getEpiodemiologist()
    if (username, password) in epidemiologist:
        print("You are an epidemiologist, you can edit the database. ")
        print("You will now be directed to the epidemiologist interface.")
        root.destroy()
        ep.goToEpidemiologist()
    elif (username, password) in people:
        print("You are a simple user, you can not edit the database.")
        print("You will now be directed to the user interface where you can select a query.")
        root.destroy()
        us.goToUserPage()
    else:
        print("You have entered the wrong data. Please retry. ")
        print("If you are not registerd yet, please click on the register Button after filling in the fields")


def getPeople():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    print("Database connected successfully")
    cur = conn.cursor()
    cur.execute("""
                    SELECT username, password
                    FROM People
                """)
    rows = cur.fetchall()
    print("All people were loaded")
    conn.close()
    return rows


def getEpiodemiologist():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    print("Database connected successfully")
    cur = conn.cursor()
    cur.execute("""
                    SELECT username, password
                    FROM Epidemiologist
                        """)
    rows = cur.fetchall()
    print("All Epidemiologist we loaded")
    conn.close()
    return rows

# Formatage de la fenêtre d'entrée
myLabelUser.grid(row=0, column=0)
myLabelPassword.grid(row=1, column=0)
EntryUser.grid(row=0, column=1)
EntryPassword.grid(row=1, column=1)
root['bg'] = 'light grey'

# Button to connect
validateButton = Button(root, text='Connect', bg='light blue', fg='black', command=controlLogIn)
validateButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=40)
root.mainloop()
