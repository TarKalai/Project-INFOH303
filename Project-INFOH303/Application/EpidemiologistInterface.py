from tkinter import *
import queries


def executeQuery(text):
    print(text)


def goToEpidemiologist():
    epidemiologistPage = Tk()
    epidemiologistPage.geometry("800x600")
    epidemiologistPage.title("Status : Epidemiologist")

    # Button first query
    firstQueryButton = Button(epidemiologistPage,
                              text='Querie 1',
                              bg='light grey',
                              command=queries.firstQuery)
    firstQueryButton.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

    # Button second query
    secondQueryButton = Button(epidemiologistPage,
                               text='Querie 2',
                               bg='light grey',
                               command=queries.secondQuery)
    secondQueryButton.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    # Button third query
    thirdQueryButton = Button(epidemiologistPage,
                              text='Querie 3',
                              bg='light grey',
                              command=queries.thirdQuery)
    thirdQueryButton.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

    # Button fourth query
    fourthQueryButton = Button(epidemiologistPage,
                               text='Querie 4',
                               bg='light grey',
                               command=queries.fourthQuery)
    fourthQueryButton.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

    # Button fifth query
    fifthQueryButton = Button(epidemiologistPage,
                              text='Querie 5',
                              bg='light grey',
                              command=queries.fifthQuery)
    fifthQueryButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    # Button sixth query
    sixthQueryButton = Button(epidemiologistPage,
                              text='Querie 6',
                              bg='light grey',
                              command=queries.sixthQuery)
    sixthQueryButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

    EntryQuery = Entry(epidemiologistPage)
    EntryQuery.grid(row=0, column=5, ipady=50, ipadx=50)
    queryButton = Button(epidemiologistPage,
                         text='execute my query',
                         bg='light grey',
                         command=lambda: executeQuery(EntryQuery.get()))
    queryButton.grid(row=1, column=5)
    epidemiologistPage.mainloop()
