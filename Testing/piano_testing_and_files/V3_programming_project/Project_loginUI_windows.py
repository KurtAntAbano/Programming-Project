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
from PIL import ImageTk, Image
from piano_TestV3 import *





# from tkinter import messagebox

def back(wx):
    wx.destroy()  # destorys any window passed into this function
    login_notebook()  # opens main again


def open_menu(w, database, email_entry, password_entry, flag):
    email = email_entry.get()
    password = password_entry.get()
    w.destroy()

    if login_verify(database, email, password):
        if flag == "user":
            userMenu(email)
        else:
            adminMenu(email)
    else:
        login_notebook()
def student_back(w, username):
    w.destroy()
    adminMenu(username)


def display_records():
    # Connect to the SQLite database
    conn = sqlite3.connect('student.db')  # Replace 'your_database.db' with your database file name
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM PROJECTS')
    records = cursor.fetchall()

    window = tk.Toplevel()
    window.title('Database Records')

    tree = ttk.Treeview(window)

    columns = [description[0] for description in cursor.description]
    tree["columns"] = columns
    tree["show"] = "headings"


    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Adjust width as needed


    for record in records:
        tree.insert("", "end", values=record)

    tree.pack(expand=True, fill="both")


    cursor.close()
    conn.close()




def on_get_index_clicked(given_tree, given_rows):
    row = given_rows
    # Get the selected index
    selected_iid = given_tree.focus()

    item_index = given_tree.index(selected_iid)
    string_to_convert = row[item_index][1]

    print(item_index)
    print(f"string:{string_to_convert}")

    list_notes = stringtolist(string_to_convert)
    print(f"list:{list_notes}")

    mainWindow = main_window()
    pianoFrame = MyPianoGUI(mainWindow, 'temp')
    pianoFrame.playback(list_notes)
    pianoFrame.destroy_GUI()






    # keyAndvalue = dict[item_index]
    # print(keyAndvalue)
    #
    # string_value = list(keyAndvalue.values())[0]
    # print(string_value)
    # #
    # # list_notes = stringtolist(string_value)
    # # print(list_notes) DICTIONARY WAS GOING TO BE USED , but a better solution was found

def student_database_window(w, givenUsername):
    w.destroy()
    teacher = givenUsername
    db_win = Tk()
    db_win.geometry("400x400")








    student_DB = studentProject()
    rows = student_DB.give_rows()
    #print(rows)
    student_DB.showAllRecords()


    #NEW IDEA: use dictionary create buttons using loop, in order to access the song strings,
    #use cget('text') to extract button text (which will be the name of user) use this calue to reference dictionary
    # and viola

    #(in order to reference the button, add the button name to a list?)





    login_label = Label(db_win, text="Student database:")
    login_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")


    backButton = Button(db_win, text="Back", command=lambda: student_back(db_win, teacher))  # passes the current window
    backButton.grid(row=1, column=4, sticky="SNEW", padx=10, pady=10)

    databaseFrame = Frame(db_win)
    databaseFrame.grid(row=10, column=0, sticky='S')
    # databaseFrame.configure(bg='black')

    label = Label(databaseFrame, text='sample test')
    label.grid(row=0, column=0)

    #  ----------------------------------------TREE VIEW-----------------------------------------------------------





    conn = sqlite3.connect('student.db')  # Replace 'your_database.db' with your database file name
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM PROJECTS')
    records = cursor.fetchall()

    # window = tk.Toplevel()
    # window.title('Database Records')

    tree = ttk.Treeview(databaseFrame)

    columns = [description[0] for description in cursor.description]
    tree["columns"] = columns
    tree["show"] = "headings"

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Adjust width as needed

    for record in records:
        tree.insert("", "end", values=record)



    tree.grid(row=0, column=0)

    btn_move = ttk.Button(databaseFrame, text="play", command=lambda:on_get_index_clicked(tree, rows))
    btn_move.grid(row=4, column=0)

    vsb = ttk.Scrollbar(databaseFrame, orient="vertical", command=tree.yview)
    #vsb.place(x=30 + 200 + 2, y=95, height=80)
    vsb.place(x=205, y=60, height=150)

    cursor.close()
    conn.close()





    def displaySongString(index):
        # song = rows[index][1]
        # print(song)

        print(index)

    dictionary = [{row[0]: row[1:]} for row in rows]

    # new_dict = {}
    # for item in dictionary:
    #     new_dict[dictionary[]] = item
    #
    # print(new_dict)

    print(dictionary)
    for d in dictionary:
        for key in d:
            if key == 'kurt':
                namee = d[key]
                print(key, namee)
    #print(dictionary[1])


    # function that creates buttons from a given list scrapped in favopur of .focus and select
    # for i in range(0, len(rows)):
    #     buttonName = f'button{rows[i][0]}'
    #     buttonName = tk.Button(databaseFrame, text=f"Button {i+1} {rows[i][0]}", command=lambda:displaySongString(rows[i][0]))
    #     buttonName.pack(side='left')

    # for i in range(0, di):
    #     buttonName = f'button{rows[i][0]}'
    #     buttonName = tk.Button(databaseFrame, text=f"Button {i+1} {rows[i][0]}", command=lambda:displaySongString(rows[i][0]))
    #     buttonName.pack(side='left')




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

    img = (Image.open(r"virtupiano_logo.png"))
    resized_img = img.resize((205, 30))
    new_img = ImageTk.PhotoImage(resized_img)
    photo_lbl = Label(userLoginWin, image=new_img)

    photo_lbl.image = new_img
    photo_lbl.grid(row=1, column=1, padx=10, pady=10, sticky="W")

    username_label = Label(userLoginWin, text="Username")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    password_label = Label(userLoginWin, text="Password")
    password_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    username_entry1 = Entry(userLoginWin, width=30)
    username_entry1.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    password_entry1 = Entry(userLoginWin, width=30)
    password_entry1.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    loginbutton = Button(userLoginWin, text="login", width=12, command=lambda: open_menu(win,
                                                                                         UseraccountDB, username_entry1,
                                                                                         password_entry1, "user"))
    loginbutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(userLoginWin, text="Exit", command=lambda: quit())
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    ################ADMIN LOGIN WINDOW###################################################

    login_label = Label(adminLoginWin, text="LOGIN DETAILS:")
    login_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    img = (Image.open(r"virtupiano_logo.png"))
    resized_img = img.resize((205, 30))
    new_img = ImageTk.PhotoImage(resized_img)
    photo_lbl = Label(adminLoginWin, image=new_img)

    photo_lbl.image = new_img
    photo_lbl.grid(row=1, column=1, padx=10, pady=10, sticky="W")

    username_label = Label(adminLoginWin, text="Username")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    password_label = Label(adminLoginWin, text="Password")
    password_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    username_entry2 = Entry(adminLoginWin, width=30)
    username_entry2.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    password_entry2 = Entry(adminLoginWin, width=30)
    password_entry2.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    loginbutton = Button(adminLoginWin, text="login", width=12, command=lambda: open_menu(win,
                                                                                          AdminaccountDB,
                                                                                          username_entry2,
                                                                                          password_entry2, "admin"))
    loginbutton.grid(row=4, column=1, padx=10, pady=10)


    skipButton = Button(adminLoginWin, text="skip", command=lambda: adminMenu('hello'))
    skipButton.grid(row=4, column=2, sticky="SNEW", padx=10, pady=10)

    backButton = Button(adminLoginWin, text="Exit", command=lambda: quit())
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    mainloop()


def adminMenu(email_entry):
    username = email_entry
    adminMenu = Tk()
    adminMenu.geometry("400x200")

    admin_label = Label(adminMenu, text="ADMIN MENU")
    admin_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    accessPiano = Button(adminMenu, text="Access \n VIRTU Piano", command=lambda:main(username))
    accessPiano.grid(row=4, column =2 , sticky="SNEW", padx=10, pady=10)

    access_db = Button(adminMenu, text="Student database", command=lambda:student_database_window(adminMenu, username))
    access_db.grid(row=4, column =3 , sticky="SNEW", padx=10, pady=10)

    deletebutton = Button(adminMenu, text="delete user", width=12, command=lambda: deleteWindow(adminMenu))
    deletebutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(adminMenu, text="Back", command=lambda: back(adminMenu))  # passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


def userMenu(email_entry):
    username = email_entry
    userMenu = Tk()
    userMenu.geometry("400x200")

    user_label = Label(userMenu, text="USER MENU")
    user_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    changebutton = Button(userMenu, text="change password", width=12, command=lambda: changePasswordwindow(userMenu,
                                                                                                           username))
    changebutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(userMenu, text="Back", command=lambda: back(userMenu))  # passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    accessPiano = Button(userMenu, text="Access \n VIRTU Piano", command=lambda:main(username))
    accessPiano.grid(row=5, column = 5, sticky="SNEW", padx=10, pady=10)


def deleteWindow(w):
    w.destroy()
    deleteMenu = Tk()
    deleteMenu.geometry("400x100")

    username_label = Label(deleteMenu, text="Username")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    userToDelete = Entry(deleteMenu, width=30)
    userToDelete.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    deleteButton = Button(deleteMenu, text="Delete", width=12, command=lambda: deleteUser(UseraccountDB,
                                                                                          userToDelete))
    deleteButton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(deleteMenu, text="Back", command=lambda: back(deleteMenu))  # passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


def changePasswordwindow(w, username):
    w.destroy()
    changeMenu = Tk()
    changeMenu.geometry("400x250")

    newPassword_label = Label(changeMenu, text="Password")
    newPassword_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    newPassword_entry = Entry(changeMenu, width=30)
    newPassword_entry.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    submitbutton = Button(changeMenu, text="submit new password", width=18,
                          command=lambda: changePassword(UseraccountDB,
                                                         username,
                                                         newPassword_entry))
    submitbutton.grid(row=5, column=1, padx=10, pady=10)

    backButton = Button(changeMenu, text="Back", command=lambda: back(changeMenu))  # passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


if __name__ == "__main__":
    UseraccountDB = login()  # creating an object
    # uncomment to test when appropriate .......

    UseraccountDB.createTable()
    UseraccountDB.insertData("kurtabano@gmail.com", "Kurt_password")
    UseraccountDB.insertData("k@gmail.com", "K")
    # accountWindow()

    AdminaccountDB = login()
    AdminaccountDB.createTable()
    AdminaccountDB.insertData("admin@gmail.com", "admin")

    login_notebook()
