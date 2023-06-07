########################################################################################################################
#  Name: Kurt
#  purpose of module: create functions for the three windows
#  bugs or notes: possibly use object orientation for them changes, make general variables for padx, pady, text colour
#  possibly create a class 'window frame' then make the login, user and admin window from it
#  USE KWARGS AND ARGS
#  date:  12/05/23
########################################################################################################################

from tkinter import *
#from tkinter import messagebox





def accountWindow():
    size = "400x180"
    loginWindow = Tk()
    loginWindow.title("login in ... ")
    loginWindow.geometry(size)

    login_label = Label(loginWindow, text="LOGIN DETAILS:")
    login_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    username_label = Label(loginWindow, text="Username")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    password_label = Label(loginWindow, text="Password")
    password_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    username_entry = Entry(loginWindow, width=30)
    username_entry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    password_entry = Entry(loginWindow, width=30)
    password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    loginbutton = Button(loginWindow, text="login", width=12) #,command = lambda: login_verify(win2, username_entry,  password_entry))
    loginbutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(loginWindow, text="Exit",command=lambda: quit())
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


    mainloop()

def adminWindow():
    adminMenu = Tk()

def userMenu():
    pass



if __name__ == "__main__":
    accountWindow()
