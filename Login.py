import sqlite3

def match_username(username):
    search_user_sql = "SELECT * FROM user WHERE username = ?"
    cursor.execute(search_user_sql,[(username)])
    return cursor.fetchall()


def match_account(username, password):
    search_user_sql = ("SELECT * FROM user WHERE username = ? AND password = ?")
    cursor.execute(search_user_sql, [(username), (password)])
    return cursor.fetchall()


def register():
    username = input("Enter a new username: ")
    firstname = input("Enter your firstname: ")
    surname = input("Enter your surname: ")
    password = input("Enter a password: ")
    ## add other information here
    
    if len(match_username(username)) != 0:
        print("Error: username taken")

    ## other validations here
        
    else:
        create_user_sql = "INSERT INTO user(username, firstname, surname, password) VALUES(?,?,?,?)"
        cursor.execute(create_user_sql, [(username), (firstname), (surname), (password)])
        db.commit()
        print("Account created. Welcome!")

with sqlite3.connect("PatientData.db") as db:
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    userID INTEGER PRIMARY KEY,
    
    username VARCHAR(20) NOT NULL,
    firstname VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL);
    ''')


## testing
username = "newUser12"
assert(match_username(username)==[])
