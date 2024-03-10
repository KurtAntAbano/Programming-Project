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

def back(window_to_destory):
    window_to_destory.destroy()  # destroys any window passed into this function
    login_notebook()  # opens login windows again


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


def index_clicked(given_tree, given_rows):
    row = given_rows
    # Get the selected index
    selected_iid = given_tree.focus()  # selects whatever the cursor is hovering

    item_index = given_tree.index(selected_iid)  # the index of the selected item is taken
    string_to_convert = row[item_index][3]  # string indexing is then used to isolate the desired record

    print(item_index)
    print(f"string:{string_to_convert}")

    list_notes = string_to_list(string_to_convert)  # remember the list of notes is in string format, so we must convert
    # it back into a list
    print(f"list:{list_notes}")

    mainWindow = main_window()
    pianoFrame = MyPianoGUI(mainWindow, 'temp', 'temp')  # an instance of the piano class is made so that I can use
    # the playback method to play the selected song
    pianoFrame.playback(list_notes)
    pianoFrame.destroy_GUI()
    #
    # keyAndvalue = dictionary_list[item_index]
    # print(keyAndvalue)
    #
    # string_value = list(keyAndvalue.values())[0]
    # print(string_value)
    #
    # list_notes = stringtolist(string_value)
    # print(list_notes) DICTIONARY WAS GOING TO BE USED , but a better solution was found


def giveFeedback(gfeedback, gscore, gtree, grows):
    feedback = gfeedback.get()
    score = gscore.get()
    if feedback == "" or score == "":

        messagebox.showinfo(title="ERROR",
                            message=f"Please fill out both entries")

    elif not score.isdigit():
        messagebox.showinfo(title="ERROR",
                            message=f"Please make sure score entry is an integer")

    elif score.isdigit():
        if int(score) >= 0 or int(score) <= 10:
            messagebox.showinfo(title="ERROR",
                                message=f"Please make sure score entry is between 0 and 10")

    else:
        confirmation_msgbox = messagebox.askyesno('Confirmation', 'Do you want to proceed')
        if confirmation_msgbox:
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
            cursor.execute("UPDATE SONG_DATABASE SET Feedback = ?, Score = ? WHERE StudentID = ? AND SongName = ?",
                           (feedback, score, selectedID, selectedSong,))

            conn.commit()
            conn.close()


def show_help():
    messagebox.showinfo(title="Help", message=f"To listen to a song, select a record from the table and click play")


def show_help_feedback():
    messagebox.showinfo(title="Help",
                        message=f"To give feedback and a score:\nSelect a record\nwrite your feedback and score\n press submit and they will be "
                                f"save in the table")


def song_table_window(w, givenUsername):
    w.destroy()
    teacher = givenUsername
    db_win = Tk()
    db_win.title("SONG TABLE")
    db_win.geometry("620x500")

    song_DB = studentProject()  # creates an instance of my song table class and uses a method to get all rows from the table
    rows = song_DB.give_rows()
    print(f"rows = {rows}")
    song_DB.showAllRecords()

    # NEW IDEA: use dictionary create buttons using loop, in order to access the song strings,
    # use cget('text') to extract button text (which will be the name of user) use this calue to reference dictionary
    # and viola

    # (in order to reference the button, add the button name to a list?)

    login_label = Label(db_win, text="Song Table:")
    login_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    backButton = Button(db_win, text="Back", command=lambda: student_back(db_win, teacher))  # passes the current window
    backButton.place(x=570, y=10)

    databaseFrame = Frame(db_win)
    databaseFrame.grid(row=10, column=0, sticky='S')

    feedbackLabel = Label(db_win, text='Feedback:')
    feedbackLabel.place(x=20, y=350)

    feedbackEntry = Entry(db_win, width=60)
    feedbackEntry.place(x=100, y=350)

    scoreLabel = Label(db_win, text='score:')
    scoreLabel.place(x=20, y=400)

    scoreEntry = Entry(db_win, width=60)
    scoreEntry.place(x=100, y=400)

    #  ----------------------------------------TREE VIEW-----------------------------------------------------------

    conn = sqlite3.connect('Student_songs.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM SONG_DATABASE')
    records = cursor.fetchall()
    print(f'records:{records}')

    tree = ttk.Treeview(databaseFrame)  # this places the tree in the database frame

    columns = [description[0] for description in
               cursor.description]  # extracts the column names from the cursor.description attribute
    tree["columns"] = columns
    tree["show"] = "headings"

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for record in records:
        tree.insert("", "end", values=record)  # inserts each record into the tree view

    tree.grid(row=0, column=0)

    btn_play = ttk.Button(db_win, text="play", command=lambda: index_clicked(tree, rows))
    btn_play.place(x=120, y=270)

    help_btn = Button(db_win, text=" ⍰ ", command=show_help)
    help_btn.place(x=200, y=270)

    tree_scroll_bar = ttk.Scrollbar(db_win, orient="vertical", command=tree.yview)
    tree_scroll_bar.place(x=580, y=60, height=150)

    cursor.close()
    conn.close()

    submit_Feedback_score = ttk.Button(db_win, text="submit feedback and score",
                                       command=lambda: giveFeedback(feedbackEntry, scoreEntry, tree, rows))
    submit_Feedback_score.place(x=100, y=450)

    feedback_help_label = Button(db_win, text=" ⍰ ", command=show_help_feedback)
    feedback_help_label.place(x=257, y=450)

    def displaySongString(row):
        print(row)

    dictionary_list = [{row[0]: row[1:]} for row in rows]

    # new_dict = {}
    # for item in dictionary:
    #     new_dict[dictionary[]] = item
    #
    # print(new_dict)

    print(dictionary_list)
    for dictionary in dictionary_list:
        for key in dictionary:
            if key == '10':
                records = dictionary[key]
                print(key, records)

    # function that creates buttons from a given list scrapped in favopur of .focus and select
    # count = 0
    # for i in range(0, len(rows)):
    #     buttonName = tk.Button(db_win, text=f"{rows[i][1]}: {rows[i][2]}", command=lambda:displaySongString(rows[i]))
    #     buttonName.place(x=0, y= count)
    #     count += 30
    #
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

    # conn = sqlite3.connect('Student_accounts.db')
    #
    # cursor = conn.cursor()
    #
    # cursor.execute('SELECT StudentName FROM USERS_DATABASE WHERE Email = ?', (email,))
    #
    # Name = cursor.fetchone()[0]
    # print(f"i found the name: {Name}")
    # return Name


def fetch_all_studentIDs():
    conn = sqlite3.connect('Student_accounts.db')

    cursor = conn.cursor()
    cursor.execute('SELECT StudentID FROM USERS_DATABASE')
    all_ids = cursor.fetchall()
    for row in all_ids:
        print(row[0])

    # print(f"these are all the ids{all_ids}")
    # print(all_ids[1])


def createAccountWindow(w):  # win1 named w so that its easier to trace
    w.destroy()  # destorys win1
    win3 = Tk()
    win3.title("Create account ... ")
    win3.geometry("400x350")

    titleLabel = Label(win3, text=" Please complete all fields ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    email_label = Label(win3, text="Email")
    email_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    password_label = Label(win3, text="Password")
    password_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    password_relabel = Label(win3, text="Re-enter Password")
    password_relabel.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    ID_label = Label(win3, text="Enter ID")
    ID_label.grid(row=5, column=0, padx=10, pady=10, sticky="W")

    user_label = Label(win3, text="Enter user")
    user_label.grid(row=6, column=0, padx=10, pady=10, sticky="W")

    email_entry = Entry(win3, width=30)
    email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    password_entry = Entry(win3, width=30)
    password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    password_reentry = Entry(win3, width=30)
    password_reentry.grid(row=4, column=1, padx=10, pady=10, sticky="E")

    ID_entry = Entry(win3, width=30)
    ID_entry.grid(row=5, column=1, padx=10, pady=10, sticky="E")

    user_entry = Entry(win3, width=30)
    user_entry.grid(row=6, column=1, padx=10, pady=10, sticky="E")

    createbutton = Button(win3, text="create account", width=12,
                          command=lambda: saveAccount(win3, email_entry, password_entry, password_reentry, ID_entry,
                                                      user_entry))
    createbutton.grid(row=7, column=1, padx=10, pady=10)

    backButton = Button(win3, text="Back", command=lambda: back(win3))  # passes the current window
    backButton.grid(row=7, column=0, sticky="SNEW", padx=10, pady=10)

    mainloop()


def saveAccount(window, givenEmail, givenPassword, givenRepassword, givenID, givenUser):
    email = givenEmail.get()
    password = givenPassword.get()
    repassword = givenRepassword.get()
    ID = givenID.get()
    user = givenUser.get()

    if is_empty_check(email, password, repassword, ID, user):  # this checks whether any fields are empty
        if is_the_same(password, repassword):  # this checks whether the passwords are the same
            conn = sqlite3.connect('Student_accounts.db')

            cursor = conn.cursor()
            cursor.execute('SELECT StudentID FROM USERS_DATABASE')
            all_ids = cursor.fetchall()
            for row in all_ids:
                if row[0] == ID:  # this checks whether the ID is unique
                    messagebox.showinfo(title="ERROR", message="ID already exists")
                    createAccountWindow(window)

            myDB = login()
            if myDB.insertData(ID, user, email, password):
                messagebox.showinfo(title="success", message="Account created successfully")
            else:
                messagebox.showinfo(title="ERROR", message="User does not exist")
        else:
            createAccountWindow(window)

    else:
        createAccountWindow(window)

        # print(row[0])
    # use insert function and add a parameter /entry for the userID


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

    skipButton = Button(adminLoginWin, text="skip", command=lambda: adminMenu("adam@gmail.com"))
    skipButton.grid(row=4, column=2, sticky="SNEW", padx=10, pady=10)

    backButton = Button(adminLoginWin, text="Exit", command=lambda: quit())
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    mainloop()


def open_piano_GUI(window, ID, name):
    window.destroy()
    Piano_main(ID, name)
    login_notebook()


def adminMenu(email_entry):
    email = email_entry
    admin_Menu = Tk()
    admin_Menu.geometry("400x200")

    admin_Menu.title("Admin_menu")

    ID_to_pass = fetch_ID(email, AdminaccountDB)
    Name_to_pass = fetch_Name(email, AdminaccountDB)

    admin_label = Label(admin_Menu, text="ADMIN MENU")
    admin_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    accessPiano = Button(admin_Menu, text="Access \n VIRTU Piano",
                         command=lambda: open_piano_GUI(admin_Menu, ID_to_pass, Name_to_pass))
    accessPiano.grid(row=4, column=2, sticky="SNEW", padx=10, pady=10)

    access_db = Button(admin_Menu, text="Song Table", command=lambda: song_table_window(admin_Menu, email))
    access_db.grid(row=4, column=3, sticky="SNEW", padx=10, pady=10)

    deletebutton = Button(admin_Menu, text="delete user", width=12, command=lambda: deleteWindow(admin_Menu))
    deletebutton.grid(row=4, column=1, padx=10, pady=10)

    createbutton = Button(admin_Menu, text="create account", width=12, command=lambda: createAccountWindow(admin_Menu))
    createbutton.grid(row=5, column=1, padx=10, pady=10)

    backButton = Button(admin_Menu, text="Back", command=lambda: back(admin_Menu))  # passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


def userMenu(email_entry):
    email = email_entry
    user_Menu = Tk()
    user_Menu.geometry("400x200")

    user_Menu.title("User_menu")

    ID_to_pass = fetch_ID(email, UseraccountDB)
    Name_to_pass = fetch_Name(email, UseraccountDB)

    user_label = Label(user_Menu, text="USER MENU")
    user_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    changebutton = Button(user_Menu, text="change password", width=12, command=lambda: changePasswordwindow(user_Menu,
                                                                                                            email))
    changebutton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(user_Menu, text="Back", command=lambda: back(user_Menu))  # passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    accessPiano = Button(user_Menu, text="Access \n VIRTU Piano",
                         command=lambda: open_piano_GUI(user_Menu, ID_to_pass, Name_to_pass))
    accessPiano.grid(row=5, column=5, sticky="SNEW", padx=10, pady=10)


def deleteWindow(window):  # this window allows users to write which user they want to delete
    window.destroy()
    deleteMenu = Tk()
    deleteMenu.geometry("400x100")
    deleteMenu.title("Delete Window")

    username_label = Label(deleteMenu, text="Email")
    username_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    userToDelete = Entry(deleteMenu, width=30)
    userToDelete.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    deleteButton = Button(deleteMenu, text="Delete", width=12, command=lambda: deleteUser(UseraccountDB,
                                                                                          userToDelete))
    # once this button is pressed a function is called which will delete the user
    deleteButton.grid(row=4, column=1, padx=10, pady=10)

    backButton = Button(deleteMenu, text="Back", command=lambda: back(deleteMenu))  # passes the current window
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


def changePasswordwindow(w, given_email):
    w.destroy()
    changeMenu = Tk()
    changeMenu.geometry("400x200")

    changeMenu.title("Change password window")

    oldPassword_label = Label(changeMenu, text="Old Password")
    oldPassword_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    oldPassword_entry = Entry(changeMenu, width=30)
    oldPassword_entry.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    confirmNew_label = Label(changeMenu, text="Confirm New Password")
    confirmNew_label.grid(row=5, column=0, padx=10, pady=10, sticky="W")

    confirmNew_entry = Entry(changeMenu, width=30)
    confirmNew_entry.grid(row=5, column=1, padx=10, pady=10, sticky="E")

    newPassword_label = Label(changeMenu, text="New Password")
    newPassword_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    newPassword_entry = Entry(changeMenu, width=30)
    newPassword_entry.grid(row=4, column=1, padx=10, pady=10, sticky="E")

    submitbutton = Button(changeMenu, text="submit new password", width=18,
                          command=lambda: changePassword(UseraccountDB,
                                                         given_email,
                                                         newPassword_entry, oldPassword_entry, confirmNew_entry))
    submitbutton.grid(row=6, column=1, padx=10, pady=10)

    backButton = Button(changeMenu, text="Back", command=lambda: back(changeMenu))  # passes the current window
    backButton.grid(row=6, column=0, sticky="SNEW", padx=10, pady=10)


if __name__ == "__main__":
    # fetch_all_studentIDs()
    UseraccountDB = login()  # creating an object
    # uncomment to test when appropriate .......

    UseraccountDB.createTable()
    UseraccountDB.insertData("30", "jett", "k@gmail.com", "K")
    # accountWindow()

    AdminaccountDB = teacher_login()
    AdminaccountDB.createTable()
    AdminaccountDB.insertData("23", "James", "adam@gmail.com", "adam")

    login_notebook()
