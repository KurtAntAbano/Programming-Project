########################################################################################################################
#  Name: Kurt
#  purpose of module: create functions for the three windows
#  bugs or notes: possibly use object orientation for them changes, make general variables for padx, pady, text colour
#  possibly create a class 'window frame' then make the login, user and admin window from it
#  USE KWARGS AND ARGS
#  date:  12/05/23
########################################################################################################################
from Project_loginUI import login_verify
from tkinter import *
from Project_SQL_accounts import login
from tkinter import ttk

#from tkinter import messagebox

def back(wx):
    wx.destroy()# destorys any window passed into this function
    login_notebook() #opens main again


def open_menu(w, database, email_entry, password_entry, flag):

    email = email_entry.get()
    password = password_entry.get()
    w.destroy()


    if login_verify(database, email, password) == True:
        if flag == "user":
            userMenu()
        else:
            adminMenu()
    else:
        login_notebook()

def login_notebook():
    win = Tk()
    win.geometry("400x200")
    # Create a Notebook widget
    my_notebook = ttk.Notebook(win)
    my_notebook.pack(expand=1, fill=BOTH)
    # Create Tabs
    userLoginWin = ttk.Frame(my_notebook)
    my_notebook.add(userLoginWin, text="User Login")
    adminLoginWin = ttk.Frame(my_notebook)
    my_notebook.add(adminLoginWin, text="Admin Login")
    # Create a Label in Tabs

    login_label = Label(userLoginWin, text="LOGIN DETAILS:")
    login_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    username_label = Label(userLoginWin, text="Username")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    password_label = Label(userLoginWin, text="Password")
    password_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    username_entry1 = Entry(userLoginWin, width=30)
    username_entry1.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    password_entry1 = Entry(userLoginWin, width=30)
    password_entry1.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    loginbutton = Button(userLoginWin, text="login", width=12, command=lambda: open_menu(win,
                                                                                           accountDB, username_entry1,
                                                                                           password_entry1, "user"))
    loginbutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(userLoginWin, text="Exit",command=lambda: quit())
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


################ADMIN LOGIN WINDOW###################################################

    login_label = Label(adminLoginWin, text="LOGIN DETAILS:")
    login_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    username_label = Label(adminLoginWin, text="Username")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    password_label = Label(adminLoginWin, text="Password")
    password_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    username_entry2 = Entry(adminLoginWin, width=30)
    username_entry2.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    password_entry2 = Entry(adminLoginWin, width=30)
    password_entry2.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    loginbutton = Button(adminLoginWin, text="login", width=12, command=lambda: open_menu(win,
                                                                                           accountDB, username_entry2,
                                                                                           password_entry2, "admin"))
    loginbutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(adminLoginWin, text="Exit", command=lambda: quit())
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


    mainloop()




def adminMenu():
    adminMenu = Tk()
    adminMenu.geometry("400x200")

    admin_label = Label(adminMenu, text = "ADMIN MENU")
    admin_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    backButton = Button(adminMenu, text="Back", command=lambda: back(adminMenu))# passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

def userMenu():
    userMenu = Tk()
    userMenu.geometry("400x200")

    user_label = Label(userMenu, text = "USER MENU")
    user_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    backButton = Button(userMenu, text="Back", command=lambda: back(userMenu))# passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)




if __name__ == "__main__":
    accountDB = login()# creating an object
    # uncomment to test when appropriate .......


    accountDB.createTable()
    accountDB.insertData("kurtabano@gmail.com", "Kurt_password")
    # accountWindow()
    login_notebook()
