# _________________________________________________________________________________#
# This file shows demo code on how to create user accounts using SQLITE3
# Created by A Issa           NOTE: all methods return True/False
# Date: 5th May 2023
# Known bugs, will be updated later
# _________________________________________________________________________________#

import sqlite3
# _________________________ Creating the class and methods __________________
class login():
    def __init__(self): # not needed, you can remove
        pass
    # _____________ method to create tables _________________________________
    def createTable(self):
        try:
            conn = sqlite3.connect('Student_accounts.db')
            #print("Opened database successfully")

            conn.execute('''CREATE TABLE IF NOT EXISTS USERS_DATABASE 
                           (StudentID TEXT PRIMARY KEY NOT NULL,
                           StudentName TEXT NOT NULL,
                           Email      TEXT     NOT NULL,
                           Password      TEXT    NOT NULL);''')

            #print("Users Accounts Table is created successfully")
            conn.close()
            return True
        except:
            return False

    # _____________ method to insert data into the table _________________________________
    def insertData(self, givenID, givenName, givenUser, givenPassword):

        try:
            conn = sqlite3.connect('Student_accounts.db')
            # insert data into database table
            conn.execute('''insert into USERS_DATABASE  (StudentID, StudentName, Email, Password) values (?, ?, ?, ?)''',
                         (givenID, givenName, givenUser, givenPassword))
            conn.commit()  # do not forget to commit the data (i.e. save the data on the table
            conn.close()
            return True
        except:
            return False

    # _____________ method to show all records stored in the table tables _________________________________

    def showAllRecords(self):
        try:
            conn = sqlite3.connect('Student_accounts.db')
            # Select all records in a table:
            cursor = conn.execute(''' SELECT StudentID, StudentName, Email, Password FROM  USERS_DATABASE ''')

            for row in cursor:
                print("ID = ", row[0])
                print("Name = ", row[1])
                print("Email = ", row[2])
                print("Passwords = ", row[3], "\n")
                return True
        except:
            return False

    # _____________ method to delete a record from the table _________________________________
    def deleteRecord(self, givenuser):
        try:
            conn = sqlite3.connect('Student_accounts.db')
            conn.execute("DELETE FROM USERS WHERE  Email =?", (givenuser,))
            print("deleted")
            conn.commit()
            conn.close()
            return True
        except:
            return False

    # _____________ method to Update password _________________________________
    def updatePassword(self, givenUser, newPassword):
        try:
            conn = sqlite3.connect('Student_accounts.db')
            conn.execute('''UPDATE USERS  SET Password = ? WHERE Email = ? ''', (newPassword, givenUser))
            conn.commit()
            conn.close()
        except:
            return False

    # _____________ method to search for a user  _________________________________
    def searchUser(self, givenUser, givenpassword):
        conn = sqlite3.connect('Student_accounts.db')
        # Select all records in a table:
        cursor = conn.execute(''' SELECT Email, Password FROM  USERS_DATABASE  ''')
        for row in cursor:
            if row[0] == givenUser and row[1] == givenpassword:
                return True
        return False


# ______________  TESTING ALL ABOVE _________________________

if __name__=="__main__":
    myDB = login() # creating an object
    # uncomment to test when appropriate .......

    myDB.createTable()
    myDB.insertData("1", "Kurt", "kurtabano@gmail.com", "Kurt_password")
    myDB.showAllRecords()
    print(myDB.searchUser("kurtabano@gmail.com", "Kurt_password"))
    # print(myDB.deleteRecord("abid2"))
    # myDB.updatePassword("abid", "newPassword")
    # print("--------------------------------")
    # myDB.showAllRecords()
