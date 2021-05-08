from tkinter import *


""""
Sélectionnez les pays qui, au même moment, ont eu au moins 5000 personnes hospitalisées
(hosp_patients);
Chaque pays doit apparaître une seule fois au maximum dans le résultat de votre requête.
"""
#
#DB_NAME = "INFO-H303"
#DB_USER = "postgres"
#DB_PASS = "root"
#DB_HOST = "localhost"
#DB_PORT = "5432"
#
#def firstQuery() :
#    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
#    print("Database connected successfully")
#    cur = conn.cursor()
#    cur.execute("""
#                SELECT iso_code
#                FROM Stat_hospitalization
#                WHERE hosp_patients >= 5000
#                GROUP BY iso_code
#                """)
#    rows = cur.fetchall()
#    for data in rows:
#        print("iso_code : " + str(data[0]))
#    print("Data selected Successfully")
#    conn.close()

def firstQuery():
    return

def secondQuery():
    return

def thirdQuery():
    return

def fourthQuery():
    return

def fifthQuery():
    return

def sixthQuery():
    return


def goToUserPage() :
    userPage = Tk()
    userPage.geometry("800x600")
    userPage.title("Status : User")

    #Button first query
    firstQueryButton = Button(userPage,
                              text = 'Countries that, at the same time,  had at least 5000 hospitalized people',
                              bg = 'light grey',
                              command=firstQuery)
    firstQueryButton.grid(row = 1, column = 0, columnspan = 2, pady =10, padx =10, ipadx = 150)

    #Button second query
    secondQueryButton = Button(userPage,
                              text='Countries that have administrated the highest total number of vaccines (1)',
                              bg = 'light grey',
                              command=secondQuery)
    secondQueryButton.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

    #Button third query
    thirdQueryButton = Button(userPage,
                              text='For each vaccine, name of the countries that use it',
                              bg = 'light grey',
                              command=thirdQuery)
    thirdQueryButton.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=205)

    #Button fourth query
    fourthQueryButton = Button(userPage,
                              text='Proportion of hospitalized population for each country on the January first 2021',
                              bg = 'light grey',
                              command=fourthQuery)
    fourthQueryButton.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

    #Button fifth query
    fifthQueryButton = Button(userPage,
                              text='Compute the evolution, for each day and each country, of the number of hospitalized patients',
                              bg = 'light grey',
                              command=fifthQuery)
    fifthQueryButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=90)

    #Button sixth query
    sixthQueryButton = Button(userPage,
                              text='Name of available vaccines in both Belgium and in France',
                              bg = 'light grey',
                              command=sixthQuery)
    sixthQueryButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=185)


    userPage.mainloop()