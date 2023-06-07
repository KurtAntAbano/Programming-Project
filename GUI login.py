from tkinter import *
from tkinter import messagebox


def back(wx):
    wx.destroy()# destorys any window passed into this function
    main() #opens main again


def main():
    # code for the main menu
    # from this window, I can go to log in or signin or exit

    win1 = Tk()
    win1.title("Welcome")
    win1.geometry("400x180")

    titleLabel = Label(win1, text=" Welcome to TKINTER programming")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    exitButton = Button(win1, text="Exit", width=12, command=quit)
    exitButton.grid(row=1, column=0, padx=10, pady=30)

    loginButton = Button(win1, text="Login", width=12, command=lambda: login(win1))
    loginButton.grid(row=1, column=1, padx=10, pady=10)

    signinButton = Button(win1, text="Sign in", width=12, command=lambda: signin(win1))#cuurent window passed
    signinButton.grid(row=1, column=2, padx=10, pady=10)

    mainloop()


def login(w):
    # code to create login screen
    w.destroy()
    win2 = Tk()
    win2.title("login in ... ")
    win2.geometry("400x180")

    login_label = Label(win2, text = "LOGIN DETAILS:")
    login_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    username_label = Label(win2, text = "Username")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    password_label = Label(win2, text = "Password")
    password_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    username_entry = Entry(win2, width = 30)
    username_entry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    password_entry = Entry(win2, width=30)
    password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    loginbutton = Button(win2, text="login", width=12, command = lambda: login_verify(win2, username_entry,  password_entry))
    loginbutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(win2, text="Back", command=lambda: back(win2))# passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

def signin(w):# win1 named w so that its easier to trace
    w.destroy()# destorys win1
    win3 = Tk()
    win3.title("Sign in ... ")
    win3.geometry("400x250")

    titleLabel = Label(win3, text=" Please complete all fields ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    username_label = Label(win3, text = "Username")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    password_label = Label(win3, text = "Password")
    password_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    password_relabel = Label(win3, text = "Re-enter Password")
    password_relabel.grid(row=4, column=0, padx=10, pady=10, sticky="W")


    username_entry = Entry(win3, width = 30)
    username_entry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    password_entry = Entry(win3, width=30)
    password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    password_reentry = Entry(win3, width=30)
    password_reentry.grid(row=4, column=1, padx=10, pady=10, sticky="E")


    createbutton = Button(win3, text="create account", width=12, command = lambda: validation(win3, username_entry, password_entry, password_reentry ))
    createbutton.grid(row=5, column=1, padx=10, pady=10)

    backButton = Button(win3, text="Back", command=lambda: back(win3))# passes the current window
    backButton.grid(row=5, column=0, sticky="SNEW", padx=10, pady=10)

    mainloop()

def validation(w, u, p, rp):
    u = u.get()
    p = p.get()
    rp = rp.get()
    if is_empty_check(w, u, p, rp) and is_the_same(w, p, rp):
        save_password(w, u, p)


def is_empty_check(w, u, p, rp):
    if u == "" or p == "" or rp == "":
        messagebox.showinfo(title="ERROR", message= "*Please make sure all fields are completed ")
        signin(w)

    else:
        return True


def is_the_same(w, p, rp):
    if p == rp:
        return True
    else:
        messagebox.showinfo(title="ERROR", message="*Passwords do not match")
        signin(w)


def save_password(w, username, password):

    f = open("user_data", "w")
    details = (username+password)
    f.write(details) # saves details on a text file that will be referenced later
    f.close()

    messagebox.showinfo(title="Success", message="*Username and Password is now registered")
    w.destroy()
    main()


def login_verify(w, username, password):

    username1 = username.get()
    password1 = password.get()

    login_details = username1 + password1
    f = open("user_data", "r")
    content = f.read()
    if login_details in content: # checks of the login details are in the text file, 'user_data'
        messagebox.showinfo(title="Success", message="*Login successful")

    else:
        messagebox.showinfo(title="ERROR", message="*Username or password does not match!")
        w.destroy()
        main()


main()