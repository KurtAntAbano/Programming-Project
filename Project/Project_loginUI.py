from Project_myValidation import is_valid_email
from Project_SQL_accounts import login


def login_verify(w, database, email_entry, password_entry):

    email = email_entry.get()
    password = password_entry.get()
    w.destroy()

    print(email, password)


    if is_valid_email(email):
        if database.searchUser(email, password):
            print("success")
        else:
            print("false")
            return True

