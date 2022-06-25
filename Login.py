import sqlite3
#from liver import HBsAb
from validation.py import *

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
    
    age = input_valid_integer("age")
    sex = input_specific_char("sex", {"M":"male", "F":"female"})
    chestPainType = input_specific_char("chest pain type", {"TA":"Typical Angina", "ATA":"Atypical Angina", "NAP":"Non-Anginal Pain", "ASY":"Asymptomatic"})
    restingBP = input_valid_integer("resting blood pressure in [mm Hg]")
    cholesterol = input_valid_float("serum cholesterol in [mm/dl]")
    fastingBS = input_valid_float("fasting blood sugar")
    chestPainType = input_specific_char("resting electrocardiogram results", {"N":"Normal", "ST":"having ST-T wave abnormality"})
    maxHR = input_valid_range("maximum heart rate achieved", 60, 202)
    exerciseAngina = input_valid_bool("exercise-induced angina")
    oldpeak = input_valid_integer("oldpeak = ST")
    stSlope = input_specific_char("slope of the peak exercise ST segment", {"U":"upsloping", "F":"flat", "D":"downsloping"})

    ALT = input_valid_integer("ALT")
    IgM = input_valid_bool("Igm")
    HBsAg = input_valid_bool("HBsAg")
    HBcAg = input_valid_bool("HBcAg")
    HBsAb = input_valid_bool("HBsAb")
    NCV = input_valid_bool("NCV")
    rateOfFatigue = input_specific_char("level of fatigue colour", {"H":"high", "N":"normal"})
    nausea = input_valid_bool("nausea")
    abdominalPain = input_valid_range("abdominal pain rating", 1, 10)
    urine = input_specific_char("urine colour", {"D":"dark", "N":"normal"})
    
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


db = sqlite3.connect("UserData.db")
cursor = db.cursor()
