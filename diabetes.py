import sqlite3

db = sqlite3.connect("UserData.db")
cursor = db.cursor()
data = cursor.fetchall()

pregnancies = data[]
glucose = data[]
bloodPressure = data[]
skinThickness = data[]
insulin = data[]
BMI = data[]

if(glucose>200):
    print("You have diabetes. Your level of glucose is greater than 200 mg/dl. Use Sulfonylureas to make insulin more efficient.")
if((glucose >140) and (glucose < 200)):
    print("You have prediabeties. Glucose is between 140 and 199 mg/dl. Watch your life style.")
if(glucose < 140):
    print("You are healthy in terms of glucose.")
if(bloodPressure > 120):
    print("Your blood pressure is too high.")
if(bloodPressure != 120/80):
    print("Your blood pressure is too high.")
if(insulin < 25):
    print("Your insulin level is good")
if(insulin >= 25):
    print("Your insulin level is too high, you have diabetes. Take Sulfonylureas. ")
if(BMI > 30):
    print("Your BPI is too big. Change your lifestyle.")
if(BMI <= 30):
    print("Your BPI is good, continue like this")    

    
cursor.close()