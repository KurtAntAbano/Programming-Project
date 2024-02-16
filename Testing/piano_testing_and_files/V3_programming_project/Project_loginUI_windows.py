########################################################################################################################
#  Name: Kurt
#  purpose of module: create functions for the three windows
#  bugs or notes: possibly use object orientation for them changes, make general variables for padx, pady, text colour
#  possibly create a class 'window frame' then make the login, user and admin window from it
#  USE KWARGS AND ARGS
#  date:  12/05/23
########################################################################################################################


from Project_loginUI_functions import login_verify, deleteUser, changePassword
from Project_myValidation import *
from Project_SQL_teacher_accountsV2 import teacher_login
from Project_SQL_student_accountsV2 import login
from tkinter import ttk
from piano_TestV3 import *
import sqlite3
from SQL_teacherV2 import studentProject





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


# def display_records():
#     conn = sqlite3.connect('Student_songs.db')
#     cursor = conn.cursor()
#
#     cursor.execute('SELECT * FROM SONG_DATABASE ')
#     records = cursor.fetchall()
#
#
#     window = tk.Toplevel()
#     window.title('Database Records')
#
#     tree = ttk.Treeview(window)
#
#     columns = [description[0] for description in cursor.description]
#     tree["columns"] = columns
#     tree["show"] = "headings"
#
#
#     for col in columns:
#         tree.heading(col, text=col)
#         tree.column(col, width=100)
#
#
#     for record in records:
#         tree.insert("", "end", values=record)
#
#     tree.pack(expand=True, fill="both")
#
#
#     cursor.close()
#     conn.close()




def on_get_index_clicked(given_tree, given_rows):
    row = given_rows
    # Get the selected index
    selected_iid = given_tree.focus()  # selects whatever the cursor is hovering

    item_index = given_tree.index(selected_iid)  # the index of the selected item is taken
    string_to_convert = row[item_index][3]  # string indexing is then used to isolate the desire record

    print(item_index)
    print(f"string:{string_to_convert}")

    list_notes = stringtolist(string_to_convert)
    print(f"list:{list_notes}")

    mainWindow = main_window()
    pianoFrame = MyPianoGUI(mainWindow, 'temp', 'temp')
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


def giveFeedback(gfeedback, gscore, gtree, grows):
    feedback = gfeedback.get()
    score = gscore.get()
    print(feedback, score)

    row = grows
    # Get the selected index
    selected_iid = gtree.focus()

    item_index = gtree.index(selected_iid)
    selectedID = row[item_index][0]

    selectedSong = row[item_index][2]
    print(selectedSong, selectedID)

    conn = sqlite3.connect('Student_songs.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE SONG_DATABASE SET Feedback = ?, Score = ? WHERE StudentID = ? AND SongName = ?", (feedback, score, selectedID, selectedSong,))

    conn.commit()
    conn.close()


def student_database_window(w, givenUsername):
    w.destroy()
    teacher = givenUsername
    db_win = Tk()
    db_win.geometry("1000x500")




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


    feedbackLabel = Label(databaseFrame, text = 'Feedback:')
    feedbackLabel.grid(row=6, column=0)

    feedbackEntry = Entry(databaseFrame, width=60)
    feedbackEntry.grid(row=6, column=1)


    scoreLabel = Label(databaseFrame, text = 'score:')
    scoreLabel.grid(row=7, column=0)

    scoreEntry = Entry(databaseFrame, width=60)
    scoreEntry.grid(row=7, column=1)



    #  ----------------------------------------TREE VIEW-----------------------------------------------------------





    conn = sqlite3.connect('Student_songs.db')  # Replace 'your_database.db' with your database file name
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM SONG_DATABASE')
    records = cursor.fetchall()

    # window = tk.Toplevel()
    # window.title('Database Records')

    tree = ttk.Treeview(databaseFrame)

    columns = [description[0] for description in cursor.description]
    tree["columns"] = columns
    tree["show"] = "headings"

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for record in records:
        tree.insert("", "end", values=record)



    tree.grid(row=0, column=0)

    btn_move = ttk.Button(databaseFrame, text="play", command=lambda:on_get_index_clicked(tree, rows))
    btn_move.grid(row=4, column=0)

    vsb = ttk.Scrollbar(databaseFrame, orient="vertical", command=tree.yview)
    #vsb.place(x=30 + 200 + 2, y=95, height=80)
    vsb.place(x=580, y=60, height=150)

    cursor.close()
    conn.close()



    saveFeedback = ttk.Button(databaseFrame, text="save project", command=lambda:giveFeedback(feedbackEntry, scoreEntry, tree, rows))
    saveFeedback.grid(row=8, column=0)



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

def fetch_ID(email, database):
    if database == AdminaccountDB:
        database_connect = 'Teacher_accounts.db'
        database_name = 'TEACHERS_DATABASE'
        ID_to_find = 'TeacherID'

    else:
        database_connect = 'Student_accounts.db'
        database_name = 'USERS_DATABASE'
        ID_to_find = 'StudentID'

    conn = sqlite3.connect(database_connect)

    cursor = conn.cursor()

    cursor.execute(f'SELECT {ID_to_find} FROM {database_name} WHERE Email = ?', (email,))

    ID = cursor.fetchone()[0]
    print(f"i found the ID: {ID}")
    return ID


def fetch_Name(email, database):
    # conn = sqlite3.connect('Student_accounts.db')
    #
    # cursor = conn.cursor()
    #
    # cursor.execute('SELECT StudentName FROM USERS_DATABASE WHERE Email = ?', (email,))
    #
    # Name = cursor.fetchone()[0]
    # print(f"i found the name: {Name}")
    # return Name
    if database == AdminaccountDB:
        database_connect = 'Teacher_accounts.db'
        database_name = 'TEACHERS_DATABASE'
        Name_to_find = 'TeacherName'

    else:
        database_connect = 'Student_accounts.db'
        database_name = 'USERS_DATABASE'
        Name_to_find = 'StudentName'

    conn = sqlite3.connect(database_connect)

    cursor = conn.cursor()

    cursor.execute(f'SELECT {Name_to_find} FROM {database_name} WHERE Email = ?', (email,))

    Name = cursor.fetchone()[0]
    print(f"i found the ID: {Name}")
    return Name




def fetch_all_studentIDs():
    conn = sqlite3.connect('Student_accounts.db')

    cursor = conn.cursor()
    cursor.execute('SELECT StudentID FROM USERS_DATABASE')
    all_ids = cursor.fetchall()
    for row in all_ids:
        print(row[0])

    # print(f"these are all the ids{all_ids}")
    # print(all_ids[1])



def createAccount(w):# win1 named w so that its easier to trace
    w.destroy()# destorys win1
    win3 = Tk()
    win3.title("Sign in ... ")
    win3.geometry("400x350")

    titleLabel = Label(win3, text=" Please complete all fields ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    email_label = Label(win3, text = "Email")
    email_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    password_label = Label(win3, text = "Password")
    password_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    password_relabel = Label(win3, text = "Re-enter Password")
    password_relabel.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    ID_label = Label(win3, text = "Enter ID")
    ID_label.grid(row=5, column=0, padx=10, pady=10, sticky="W")

    user_label = Label(win3, text = "Enter user")
    user_label.grid(row=6, column=0, padx=10, pady=10, sticky="W")




    email_entry = Entry(win3, width = 30)
    email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    password_entry = Entry(win3, width=30)
    password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    password_reentry = Entry(win3, width=30)
    password_reentry.grid(row=4, column=1, padx=10, pady=10, sticky="E")

    ID_entry = Entry(win3, width=30)
    ID_entry.grid(row=5, column=1, padx=10, pady=10, sticky="E")

    user_entry = Entry(win3, width=30)
    user_entry.grid(row=6, column=1, padx=10, pady=10, sticky="E")



    createbutton = Button(win3, text="create account", width=12, command = lambda: saveAccount(win3, email_entry, password_entry, password_reentry, ID_entry, user_entry))
    createbutton.grid(row=7, column=1, padx=10, pady=10)

    backButton = Button(win3, text="Back", command=lambda: back(win3))# passes the current window
    backButton.grid(row=7, column=0, sticky="SNEW", padx=10, pady=10)

    mainloop()

def saveAccount(window, givenEmail, givenPassword, givenRepassword, givenID, givenUser):

    email = givenEmail.get()
    password = givenPassword.get()
    repassword = givenRepassword.get()
    ID = givenID.get()
    user = givenUser.get()

    if is_empty_check(email, password, repassword, ID, user):
        if is_the_same(password, repassword):
            conn = sqlite3.connect('Student_accounts.db')

            cursor = conn.cursor()
            cursor.execute('SELECT StudentID FROM USERS_DATABASE')
            all_ids = cursor.fetchall()
            for row in all_ids:
                if row[0] == ID:
                    messagebox.showinfo(title="ERROR", message="ID already exists")
                    createAccount(window)


            myDB = login()
            myDB.insertData(ID, user, email, password)
        else:
            messagebox.showinfo(title="ERROR", message="passwords do not match")
            createAccount(window)

    else:
        createAccount(window)








            # print(row[0])
    #use insert function and add a parameter /entry for the userID
    



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

    win.title("Login")


    login_label = Label(userLoginWin, text="LOGIN DETAILS:")
    login_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    img = (Image.open(r"virtupiano_logo.png"))
    resized_img = img.resize((205, 30))
    new_img = ImageTk.PhotoImage(resized_img)
    photo_lbl = Label(userLoginWin, image=new_img)

    photo_lbl.image = new_img
    photo_lbl.grid(row=1, column=1, padx=10, pady=10, sticky="W")

    username_label = Label(userLoginWin, text="Email")
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

    username_label = Label(adminLoginWin, text="Email")
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


    skipButton = Button(adminLoginWin, text="skip", command=lambda: adminMenu("admin@gmail.com"))
    skipButton.grid(row=4, column=2, sticky="SNEW", padx=10, pady=10)

    backButton = Button(adminLoginWin, text="Exit", command=lambda: quit())
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    mainloop()


def adminMenu(email_entry):
    username = email_entry
    adminMenu = Tk()
    adminMenu.geometry("400x200")

    ID_to_pass = fetch_ID(username, AdminaccountDB)
    Name_to_pass = fetch_Name(username, AdminaccountDB)


    admin_label = Label(adminMenu, text="ADMIN MENU")
    admin_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    accessPiano = Button(adminMenu, text="Access \n VIRTU Piano", command=lambda:main(ID_to_pass, Name_to_pass))
    accessPiano.grid(row=4, column =2 , sticky="SNEW", padx=10, pady=10)

    access_db = Button(adminMenu, text="Student database", command=lambda:student_database_window(adminMenu, username))
    access_db.grid(row=4, column =3 , sticky="SNEW", padx=10, pady=10)

    deletebutton = Button(adminMenu, text="delete user", width=12, command=lambda: deleteWindow(adminMenu))
    deletebutton.grid(row=4, column=1, padx=10, pady=10)

    createbutton = Button(adminMenu, text="create account", width=12, command=lambda: createAccount(adminMenu))
    createbutton.grid(row=5, column=1, padx=10, pady=10)

    backButton = Button(adminMenu, text="Back", command=lambda: back(adminMenu))  # passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


def userMenu(email_entry):
    username = email_entry
    userMenu = Tk()
    userMenu.geometry("400x200")


    ID_to_pass = fetch_ID(username, UseraccountDB)
    Name_to_pass = fetch_Name(username, UseraccountDB)

    user_label = Label(userMenu, text="USER MENU")
    user_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    changebutton = Button(userMenu, text="change password", width=12, command=lambda: changePasswordwindow(userMenu,
                                                                                                           username))
    changebutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(userMenu, text="Back", command=lambda: back(userMenu))  # passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    accessPiano = Button(userMenu, text="Access \n VIRTU Piano", command=lambda:main(ID_to_pass, Name_to_pass))
    accessPiano.grid(row=5, column = 5, sticky="SNEW", padx=10, pady=10)


def deleteWindow(w):
    w.destroy()
    deleteMenu = Tk()
    deleteMenu.geometry("400x100")

    username_label = Label(deleteMenu, text="Email")
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
    #fetch_all_studentIDs()
    UseraccountDB = login()  # creating an object
    # uncomment to test when appropriate .......

    UseraccountDB.createTable()
    UseraccountDB.insertData("30", "jett", "k@gmail.com", "K")
    # accountWindow()

    AdminaccountDB = teacher_login()
    AdminaccountDB.createTable()
    AdminaccountDB.insertData("23", "James", "adam@gmail.com", "adam")

    login_notebook()