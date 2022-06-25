#if(ALT > 36):you have a liber problem
#AST

import sqlite3

#Rate of fatigue
#Nausea and vomiting
#Abdominal pain
#urine color (Dark is bad)

#For hepatitsA, IgM antiboundies found => yoiu have hepatits A, else no
#For hepatitisB, HBsAg and HBcAb found you are ingected. If you have HBsAb you are protected.
#For hepatitis C, reactive HCV antibody you have it, else (non-reactive), you are good

db = sqlite3.connect("UserData.db")
cursor = db.cursor()
data = cursor.fetchall()

ALT = data[11]
IgM = data[12]
HBsAg = data[13]
HBcAb = data[14]
HBsAb = data[15]
NCV = data[16]
rateOfFatigue = data[17]
nausea = data[18]
abdominalPain =  data[19]
urine = data[20]


if(ALT > 36):
    print("You have a liver problem.")
    if(IgM == "Y"):
        print("You have hepatitis A. There is no treatment. Rest and take painkillers.")
    if(HBsAg == "Y"):
        print("You are safe against hepatitis B.")
    if((HBsAg == "N") and ((HBsAg == "Y") or (HBcAb == "Y"))):
        print("You have hepatitis B. Take a pil of Viread once a day for at least one year")
    if(NCV == "Y"):
        print("You have hepatitis C. Take a pil of Daklinza for a few weeks.")
    if(NCV == "N"):
        print("You don't have hepatitis C.")
else:
    if(rateOfFatigue == "H"):
        print("Try to rest. Go in bed. Sleep more")
    if(nausea == "yY"):
        print("Take Zofran until you don't have nausea.")
    if(abdominalPain > 5):
        print("Rest.")
    if(urine == "D"):
        print("Investigate more")
    else:
        print("Take care of yourself. You are fine!")
    
cursor.close()
