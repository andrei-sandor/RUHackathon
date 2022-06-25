import sqlite3
from liver import HBsAb

def username_match(username):
    search_user_sql = "SELECT * FROM user WHERE username = ?"
    cursor.execute(search_user_sql,[(username)])
    if len(cursor.fetchall()) == 1:
        return True
    return False

def account_match(username, password):
    search_user_sql = ("SELECT * FROM user WHERE username = ? AND password = ?")
    cursor.execute(search_user_sql, [(username), (password)])
    if len(cursor.fetchall()) == 1:
        return True
    return False

def register_user():
    username = input("Enter a new username: ")
    firstname = input("Enter your firstname: ")
    surname = input("Enter your surname: ")
    password = input("Enter a password: ")
    user_type = input("Enter P for patient or D for doctor: ")

    if not username_match:
        print("Error: username taken")
    elif user_type not in ["P" or "D"]:
        print("Error: must enter P for patient or D for doctor")

    else:
        register_user_sql = "INSERT INTO user(username, firstname, surname, password) VALUES(?,?,?,?,?)"
        cursor.execute(register_user_sql, [(username), (firstname), (surname), (password), (user_type)])
        db.commit()
        print("User account created. Welcome!")

        if patient_code == "P":
            register_patient()
        else:
            register_doctor()

def register_patient(username):
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

    ALT = input("Enter the value of your ALT: ")
    IgM = input("Enter yes if you have IgM: ")
    HBsAg = input("Enter yes if you have HBsAg: ")
    HBcAg = input("Enter yes if you have HBcAg: ")
    HBsAb = input("Enter yes if you have HBsAb: ")
    NCV = input("Enter yes if you have NCV: ")
    rateOfFatigue = input("Enter you rate of fatigue (High or Normal: ")
    nausea = input("Enter yes if you have nausea: ")
    abdominalPain = input("Enter on a scale from 1 to 10 how much abdominal pain you have: ")
    urine = input("Enter the color of your urine (Dark or Normal: ")
    
    register_patient_sql = """INSERT INTO patient(age, sex, chestPainType, restingBP, cholesterol, fastingBS, restingECG, maxHR,
                                exerciseAngina, oldpeak, stSlope, ALT, IgM, HBsAg, HBcAg, HBsAg, NCV, rateOfFatigue, nausea, abdominalPain, urine, userID) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    cursor.execute(register_patient_sql, [(age), (sex), (chestPainType), (restingBP), (cholesterol), (fastingBS), (restingECG), (maxHR), (exerciseAngina), (oldpeak), (stSlope)
                                          ,(ALT), (IgM), (HBsAg), (HBcAg), (HBsAb), (NCV), (rateOfFatigue), (nausea), (abdominalPain), (urine), (username)])
    db.commit()
    print("Patient account created. Welcome!")
    
def register_doctor():
    pass

def login_user():
    username = input("Enter a username")
    password = input("Enter a password")
    if not username_match(username):
        print("Username not recognised. Please try again")
    elif not account_match(username, password):
        print("Password is incorrect. Please try again")
    else:
        global username


db = sqlite3.connect("UserData.db")
cursor = db.cursor()
