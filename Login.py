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

def inputHeart():
    
    connection = sqlite3.connect("HearthData.db")
    
    cursor = connection.cursor()
    
    age = input("Enter your age: ")
    sex = input("Enter your sex: ")
    chestPainType = input("Enter your chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]: ")
    restingBP = input("Enter your resting blood pressure [mm Hg]: ")
    cholesterol = input("Enter your serum cholesterol [mm/dl]: ")
    fastingBS = input("Enter your fasting blood sugar: ")
    restingECG = input(" Enter your resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV ]: ")
    maxHR = input("Enter your maximum heart rate achieved [Numeric value between 60 and 202]: ")
    exerciseAngina = input("Enter your exercise-induced angina [Y: Yes, N: No]: ")
    oldpeak = input("Enter your oldpeak = ST [Numeric value measured in depression]: ")
    stSlope = input("Enter you slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]: ")
    
    cursor.execute(age,sex,chestPainType,restingBP,cholesterol,fastingBS,restingECG,maxHR,exerciseAngina,oldpeak,stSlope)
    print("Table Created")
    connection.commit()
    
    

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