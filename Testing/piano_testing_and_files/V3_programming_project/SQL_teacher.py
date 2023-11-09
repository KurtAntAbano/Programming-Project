# _________________________________________________________________________________#
# This file shows demo code on how to create user accounts using SQLITE3
# Created by A Issa           NOTE: all methods return True/False
# Date: 5th May 2023
# Known bugs, will be updated later
# _________________________________________________________________________________#

import sqlite3
# _________________________ Creating the class and methods __________________
class studentProject():
    def __init__(self): # not needed, you can remove
        pass
    # _____________ method to create tables _________________________________
    def createTable(self):
        try:
            conn = sqlite3.connect('student.db')
            #print("Opened database successfully")

            conn.execute('''CREATE TABLE IF NOT EXISTS PROJECTS
                           (User      TEXT     PRIMARY KEY     NOT NULL,
                            project      TEXT    NOT NULL);''')

            #print("Users Accounts Table is created successfully")
            conn.close()
            return True
        except:
            return False

    # _____________ method to insert data into the table _________________________________
    def insertData(self, givenUser, givenPassword):

        try:
            conn = sqlite3.connect('student.db')
            # insert data into database table
            conn.execute('''insert into PROJECTS  (User, project) values (?, ?)''',
                         (givenUser, givenPassword))
            conn.commit()  # do not forget to commit the data (i.e. save the data on the table
            conn.close()
            return True
        except:
            return False

    # _____________ method to show all records stored in the table tables _________________________________

    def showAllRecords(self):
        try:
            conn = sqlite3.connect('student.db')
            # Select all records in a table:
            cursor = conn.cursor()
            cursor.execute(''' SELECT User, project FROM  PROJECTS ''')

            rows = cursor.fetchall()



            print("Number of rows:", len(rows))

            for row in rows:
                print("User Name = ", row[0])
                print("Passwords = ", row[1], "\n")

            return True

        except:
            return False

    def give_rows(self):
        conn = sqlite3.connect('student.db')
        # Select all records in a table:
        cursor = conn.cursor()
        cursor.execute(''' SELECT User, project FROM  PROJECTS ''')

        rows = cursor.fetchall()
        return rows


    # _____________ method to delete a record from the table _________________________________
    def deleteRecord(self, givenuser):
        try:
            conn = sqlite3.connect('student.db')
            conn.execute("DELETE FROM PROJECTS WHERE  User =?", (givenuser,))
            print("deleted")
            conn.commit()
            conn.close()
            return True
        except:
            return False

    # _____________ method to Update password _________________________________
    def updatePassword(self, givenUser, newPassword):
        try:
            conn = sqlite3.connect('student.db')
            conn.execute('''UPDATE PROJECTS  SET project = ? WHERE User = ? ''', (newPassword, givenUser))
            conn.commit()
            conn.close()
        except:
            return False

    # _____________ method to search for a user  _________________________________
    def searchUser(self, givenUser, givenpassword):
        conn = sqlite3.connect('student.db')
        # Select all records in a table:
        cursor = conn.execute(''' SELECT User, project FROM  PROJECTS ''')
        for row in cursor:
            if row[0] == givenUser and row[1] == givenpassword:
                return True
        return False


# ______________  TESTING ALL ABOVE _________________________

if __name__=="__main__":
    student_DB = studentProject() # creating an object
    # uncomment to test when appropriate .......

    student_DB.createTable()
    student_DB.insertData("kurt", "a string")
    student_DB.insertData("anthony", "hello world")
    student_DB.showAllRecords()
    #print(student_DB.searchUser("kurtabano@gmail.com", "Kurt_password"))
    print(student_DB.searchUser("kurt", "a string"))
    print(student_DB.give_rows())
    # print(myDB.deleteRecord("abid2"))
    # myDB.updatePassword("abid", "newPassword")
    # print("--------------------------------")
    # myDB.showAllRecords()
