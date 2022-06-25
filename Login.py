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
    IgM = input("Enter Y if you have IgM and N if you do not: ")
    HBsAg = input("Enter Y if you have HBsAg and N if you do not: ")
    HBcAg = input("Enter Y if you have HBcAg and N if you do not: ")
    HBsAb = input("Enter Y if you have HBsAb and N if you do not: ")
    NCV = input("Enter Y if you have NCV and N if you do not: ")
    rateOfFatigue = input("Enter H for a high rate of fatigue or N for Normal: ")
    nausea = input("Enter Y if you have nausea and N if you do not: ")
    abdominalPain = input("Enter on a scale from 1 to 10 how much abdominal pain you have: ")
    urine = input("Enter D if you have dark urine or N if it is a normal colour: ")
    
    pregnancies = input("Enter Y if you plan to be pregnant: ")
    glucose = input("Enter the plasma glucose concentration for 2 hours in an oral glucose tolerance test: ")
    bloodPressure = input("Enter your diastolic blood pressure (mm Hg): ")
    skinThickness = input("Enter your triceps skin fold thickness (mm): ")
    insulin = input("Enter your 2-Hour serum insulin (mu U/ml): ")
    BMI = input("Enter your body mass index (weight in kg/(height in m)^2): ")
    
    
    register_patient_sql = """INSERT INTO patient(age, sex, chestPainType, restingBP, cholesterol, fastingBS, restingECG, maxHR,
                                exerciseAngina, oldpeak, stSlope, ALT, IgM, HBsAg, HBcAg, HBsAg, NCV, rateOfFatigue, nausea, abdominalPain, urine, pregnancies, glucose, bloodPressure, skinThickness, insulin, BMI, userID) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    cursor.execute(register_patient_sql, [(age), (sex), (chestPainType), (restingBP), (cholesterol), (fastingBS), (restingECG), (maxHR), (exerciseAngina), (oldpeak), (stSlope)
                                          ,(ALT), (IgM), (HBsAg), (HBcAg), (HBsAb), (NCV), (rateOfFatigue), (nausea), (abdominalPain), (urine), (pregnancies), (glucose), (bloodPressure), (skinThickness), (insulin), (BMI) (username)])
    db.commit()
    print("Patient account created. Welcome!")
    

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
