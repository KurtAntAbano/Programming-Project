########################################################################################################################
#  Name: Kurt
#  purpose of module: create functions for the three windows
#  bugs or notes: possibly use object orientation for them changes, make general variables for padx, pady, text colour
#  possibly create a class 'window frame' then make the login, user and admin window from it
#  USE KWARGS AND ARGS
#  date:  12/05/23
########################################################################################################################
from Project_loginUI_functions import login_verify, deleteUser, changePassword
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


    if login_verify(database, email, password):
        if flag == "user":
            userMenu(email)
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

    deletebutton = Button(adminMenu, text="delete user", width=12, command=lambda: deleteWindow(adminMenu))
    deletebutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(adminMenu, text="Back", command=lambda: back(adminMenu))# passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)



def userMenu(email_entry):
    username = email_entry
    userMenu = Tk()
    userMenu.geometry("400x200")

    user_label = Label(userMenu, text = "USER MENU")
    user_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    changebutton = Button(userMenu, text="change password", width=12, command=lambda: changePasswordwindow(userMenu,
                                                                                                           username))
    changebutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(userMenu, text="Back", command=lambda: back(userMenu))# passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


def deleteWindow(w):
    w.destroy()
    deleteMenu = Tk()
    deleteMenu.geometry("400x100")

    username_label = Label(deleteMenu, text="Username")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    userToDelete = Entry(deleteMenu, width=30)
    userToDelete.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    deleteButton = Button(deleteMenu, text="Delete", width=12, command=lambda: deleteUser(accountDB,
                                                                                        userToDelete))
    deleteButton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(deleteMenu, text="Back", command=lambda: back(deleteMenu))# passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


def changePasswordwindow(w, username):
    w.destroy()
    changeMenu = Tk()
    changeMenu.geometry("400x250")

    newPassword_label = Label(changeMenu, text = "Password")
    newPassword_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    newPassword_entry = Entry(changeMenu, width=30)
    newPassword_entry.grid(row=3, column=1, padx=10, pady=10, sticky="E")


    submitbutton = Button(changeMenu, text="submit new password", width=18, command = lambda: changePassword(accountDB,
                                                                                                        username,
                                                                                                        newPassword_entry))
    submitbutton.grid(row=5, column=1, padx=10, pady=10)

    backButton = Button(changeMenu, text="Back", command=lambda: back(changeMenu))# passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)





if __name__ == "__main__":
    accountDB = login()# creating an object
    # uncomment to test when appropriate .......


    accountDB.createTable()
    accountDB.insertData("kurtabano@gmail.com", "Kurt_password")
    # accountWindow()
    login_notebook()
