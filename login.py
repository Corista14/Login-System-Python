# Developed by Filipe Corista
# Simple login system using python and sqlite

import sqlite3
import bcrypt


# Database connection
conn = sqlite3.connect('coristheforis.db')
conn.execute("""CREATE TABLE IF NOT EXISTS Coris (
                username text,
                password text
)""")


def home():
    print("------------ Welcome to CorisTheForis' App ------------")
    print("Do you own an account? (Y/N): ")

    has_account_input = input("").upper()

    # Call Login function if the user has an account
    if has_account_input == "Y":
        login()

    # Call Register Function if the user does not has an account
    elif has_account_input == "N":
        register()

    else:
        print("Sorry, you have to type either 'Y'(Yes) or 'N'(No).")
        home()



def login():
    print("------------ Login into CorisTheForis' App ------------")

    """
    print("Enter your username: ")
    username = input("")

    # If the username input is NOT empty, the user can enter the password
    if username != "":
        print("Enter your password: ")
        password = input("")

    # If not, the user has to make the login form again
    else:
        print("Provide a username!")
        login()
    """


def register():
    print("------------ Register into CorisTheForis' App ------------")
    print("Enter your desired username: ")
    username = input("")

    # If the username input is NOT empty, the user can enter the password
    if username != "":
        print("Enter your super secret desired password: ")
        password_input = input("").encode('utf-8') # We must encode the password to convert the String into Bytes before hashing it
        hashed_password = bcrypt.hashpw(password_input, bcrypt.gensalt()) # Hash the password in order to secure it
        
        # We must decode the password to convert from Byte to String before inserting into the DB
        conn.execute("INSERT INTO Coris VALUES ('{}', '{}')".format(
            username, hashed_password.decode('utf-8'))) 

        conn.commit()  # Submit the values to the database
        conn.close()  # Close DB

        print("Succecefuly created the account!!!")
        home()

    # If it is, the user has to make the register form again
    else:
        print("Provide a password!")
        register()


home()
