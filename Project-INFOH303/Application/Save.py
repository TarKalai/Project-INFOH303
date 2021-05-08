from tkinter import *

#Initialise Connection Page
root = Tk()
root.title("Base de données Covid - Visiteur")
root.geometry("300x200")
myLabelUser = Label(root, text= "Username : ")
myLabelPassword = Label(root, text= "Password : ")
EntryUser= Entry(root)
EntryPassword= Entry(root)


def controlLogIn():
    """
    Vérifie le type d'utilisateur dans l'application pour aller à la bonne page suivante
    :return: void
    """
    username = EntryUser.get()
    password = EntryPassword.get()
    if username == "david":
        root.destroy()
        goToUserPage()
    elif username == "Seb":
        root.destroy()
        goToEpidemiologistPage()
    else :
        print("Vous n'êtes pas enregistré")


def goToEpidemiologistPage():
    epidemiologistPage = Tk()
    epidemiologistPage.geometry("500x500")
    epidemiologistPage.title("Status : Epidemiologist")


def goToUserPage():
    userPage = Tk()
    userPage.geometry("500x500")
    userPage.title("Status : User")

def firstQuery():
    return


#Button first query
firstQueryButton = Button(userPage, text = 'les pays qui, au même moment, ont eu au moins 5000 personnes hospitalisées', command=firstQuery)
firstQueryButton.grid(row = 2, column = 0, columnspan = 2, pady =10, padx =10, ipadx = 150)

# Button to connect
validateButton = Button(newPage, text = 'Connect', command=controlLogIn)
validateButton.grid(row = 4, column = 0, columnspan = 2, pady =10, padx =10, ipadx = 40)



# Formatage de la fenêtre d'entrée
myLabelUser.grid(row=0, column=0)
myLabelPassword.grid(row=2, column=0)
EntryUser.grid(row = 0, column=1)
EntryPassword.grid(row=2, column=1)

"""Rechercher comment packer la fenetre"""
#EntryUser.pack()
#EntryPassword.pack()
#validateButton.pack()

root.mainloop()

