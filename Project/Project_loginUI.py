from Project_myValidation import is_valid_email
from Project_SQL_accounts import login


def login_verify(w, email_entry, password_entry):
    #w.destroy()

    email = email_entry.get()
    password = password_entry.get()

    if is_valid_email(email):
        if login.searchUser(email, password):
            print("success")
            return True
