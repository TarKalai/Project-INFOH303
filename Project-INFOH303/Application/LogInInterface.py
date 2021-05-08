from tkinter import *
import UserInterface as us
import EpidemiologistInterface as ep

#Initialise Connection Page
root = Tk()
root.title("Base de données Covid - Visiteur")
root.geometry("300x200")
myLabelUser = Label(root, text= "Username : ")
myLabelPassword = Label(root, text= "Password : ")
myLabelPassword.place(x = 400)
EntryUser= Entry(root)
EntryPassword= Entry(root)
EntryPassword.place(x= 400)

userDico = {'tarik' : "1", 'seb' : "2", 'david' : "3"}
epidDico = {'Zimanyi' : "0"}


def controlLogIn():
    """
    Vérifie le type d'utilisateur dans l'application pour aller à la bonne page suivante
    :return: void
    """
    username = EntryUser.get()
    password = EntryPassword.get()
    if (username in userDico and userDico.get(username)==password):
        print("You are a simple user, you can not edit the database.")
        print("You will now be directed to the user interface where you can select a query.")
        root.destroy()
        us.goToUserPage()
    elif (username in epidDico and epidDico.get(username)==password):
        print("You are an epidemiologist, you can edit the database. ")
        print("You will now be directed to the epidemiologist interface.")
        root.destroy()
        ep.goToEpidemiologist()
    else :
        print("You have entered the wrong data. Please retry. ")
        print("If you are not registerd yet, please click on the register Button after filling in the fields")

# Formatage de la fenêtre d'entrée
myLabelUser.grid(row=0, column=0)
myLabelPassword.grid(row=2, column=0)
EntryUser.grid(row = 0, column=1)
EntryPassword.grid(row=2, column=1)
root['bg'] = 'light grey'

def join():
    """
    TO DO
    :return:
    """
    newUserName = EntryUser.get()
    newPassword = EntryPassword.get()



# Button to connect
validateButton = Button(root, text = 'Connect', bg = 'light blue', fg = 'black', command=controlLogIn)
validateButton.grid(row = 4, column = 0, columnspan = 2, pady =10, padx =10, ipadx = 40)

#Button to register
registerButton = Button(root, text = "Register", bg = 'light grey', command = join)
registerButton.grid(row = 5, column = 0, columnspan = 2, pady =10, padx =10, ipadx = 40 )
root.mainloop()

