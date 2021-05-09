from tkinter import *
import queries


def goToUserPage():
    userPage = Tk()
    userPage.geometry("800x600")
    userPage.title("Status : User")

    # Button first query
    firstQueryButton = Button(userPage,
                              text='Countries that, at the same time,  had at least 5000 hospitalized people',
                              bg='light grey',
                              command=queries.firstQuery)
    firstQueryButton.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=150)

    # Button second query
    secondQueryButton = Button(userPage,
                               text='Countries that have administrated the highest total number of vaccines (1)',
                               bg='light grey',
                               command=queries.secondQuery)
    secondQueryButton.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

    # Button third query
    thirdQueryButton = Button(userPage,
                              text='For each vaccine, name of the countries that use it',
                              bg='light grey',
                              command=queries.thirdQuery)
    thirdQueryButton.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=205)

    # Button fourth query
    fourthQueryButton = Button(userPage,
                               text='Proportion of hospitalized population for each country on the January first 2021',
                               bg='light grey',
                               command=queries.fourthQuery)
    fourthQueryButton.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

    # Button fifth query
    fifthQueryButton = Button(userPage,
                              text='Compute the evolution, for each day and each country, of the number of hospitalized patients',
                              bg='light grey',
                              command=queries.fifthQuery)
    fifthQueryButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=90)

    # Button sixth query
    sixthQueryButton = Button(userPage,
                              text='Name of available vaccines in both Belgium and France',
                              bg='light grey',
                              command=queries.sixthQuery)
    sixthQueryButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=185)

    userPage.mainloop()
