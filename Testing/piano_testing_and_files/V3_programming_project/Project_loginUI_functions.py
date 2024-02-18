from Project_myValidation import is_valid_email, presenceCheck
from tkinter import messagebox
# from Project_loginUI_windows import adminMenu, userMenu


def login_verify(database, email, password):
    if presenceCheck(email) and presenceCheck(password):
        if database.searchUser(email, password):
            messagebox.showinfo(title="Success", message="*Login successful")
            return True
        else:
            messagebox.showinfo(title="ERROR", message="*Username or password does not match!")
            return False
    else:
        messagebox.showinfo(title="ERROR", message="*Please make sure all fields are completed ")
        return False


    # if presenceCheck(email) and presenceCheck(password):
    #     if is_valid_email(email):
    #         if database.searchUser(email, password):
    #             messagebox.showinfo(title="Success", message="*Login successful")
    #             return True
    #         else:
    #             messagebox.showinfo(title="ERROR", message="*Username or password does not match!")
    #             return False
    #     else:
    #         messagebox.showinfo(title="ERROR", message="*incorrect format!")
    #
    # else:
    #     messagebox.showinfo(title="ERROR", message= "*Please make sure all fields are completed ")
    #     return False

def deleteUser(database, username_entry):
    username = username_entry.get()
    #  depending on the outcome of the deletion appropriate message boxes show to the teacher
    if database.deleteRecord(username) == False:  # database.deleteRecord() is a method from the database SQL class python file
        messagebox.showinfo(title="ERROR", message="*User does not exist")
    else:
        messagebox.showinfo(title="SUCCESS", message="*User deleted")

def changePassword(database, email, newPassword):
    password = newPassword.get()


    if database.updatePassword(email, password) == False:
        messagebox.showinfo(title="ERROR", message="*User does not exist")
    else:
        messagebox.showinfo(title="SUCCESS", message="*Password changed")
