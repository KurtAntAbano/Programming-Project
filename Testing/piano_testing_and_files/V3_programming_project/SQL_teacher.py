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
    student_DB.insertData("focalors", "1700518497.0799303,E0,1.1353676319122314,D0,0.7319555282592773,C0,0.35520434379577637,B-1,1.5408971309661865,E-1,0.3579287528991699,F#-1,0.37304186820983887,G-1,0.3585524559020996,A-1,0.32934093475341797,B-1,0.38792872428894043,A-1,0.34629392623901367,G-1,0.37407493591308594,E-1,0.3712480068206787,G-1,1.273707389831543,F#-1")
    student_DB.showAllRecords()
    student_DB.insertData("ffffff", "1700584909.9782283,E0,1.0877537727355957,D0,0.7495157718658447,C0,0.33042025566101074,B-1,1.5811004638671875,E-1,0.35768961906433105,F#-1,0.34398460388183594,G-1,0.38354921340942383,A-1,0.3762960433959961,B-1,0.36725473403930664,A-1,0.34379005432128906,G-1,0.3540792465209961,E-1,0.3878793716430664,G-1,1.2282843589782715,F#-1")
    #print(student_DB.searchUser("kurtabano@gmail.com", "Kurt_password"))
    print(student_DB.searchUser("kurt", "a string"))
    print(student_DB.give_rows())
    # print(myDB.deleteRecord("abid2"))
    # myDB.updatePassword("abid", "newPassword")
    # print("--------------------------------")
    # myDB.showAllRecords()
