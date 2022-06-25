import sqlite3

with sqlite3.connect("UserData.db") as db:
    cursor = db.cursor()

    ## create user table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    username VARCHAR(20) PRIMARY KEY,
    firstname VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    user_type CHAR NOT NULL);
    ''')

    ## create patient table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patient(
    age INTEGER NOT NULL,
    sex CHAR NOT NULL,
    chestPainType VARCHAR(3) NOT NULL,
    restingBP INTEGER NOT NULL,
    cholesterol VARCHAR(10) NOT NULL,
    fastingBS VARCHAR(10) NOT NULL,
    restingECG VARCHAR(6) NOT NULL,
    maxHR INTEGER NOT NULL,
    exerciseAngina CHAR NOT NULL,
    oldpeak VARCHAR(10) NOT NULL,
    stSlope VARCHAR(4) NOT NULL,
    username VARCHAR(20) PRIMARY KEY,
    FOREIGN KEY(username) REFERENCES user(username));
    ''')

    ## first registering the patients in user table
    register_user_sql = "INSERT INTO user(username, firstname, surname, password, user_type) VALUES(?,?,?,?,?)"
    cursor.execute(register_user_sql, [("StewartSmith12"), ("Stewart"), ("Smith"), ("hx61s7cns"), ("P")])
    cursor.execute(register_user_sql, [("ARoy"), ("Amanda"), ("Roy"), ("kbads762m"), ("P")])
    cursor.execute(register_user_sql, [("Lolalala"), ("Lola"), ("Kwa"), ("adh796342n"), ("P")])
    cursor.execute(register_user_sql, [("KHam14"), ("Kwami"), ("Hamilton"), ("iad723n10934"), ("P")])
    cursor.execute(register_user_sql, [("1Kish3"), ("Kishami"), ("Ruhaama"), ("08234basm"), ("P")])
    cursor.execute(register_user_sql, [("JohnJohn"), ("John John"), ("Florencia"), ("2uhlascn"), ("P")])

    ## then adding patient data in patient table
    register_patient_sql = "INSERT INTO patient(username, firstname, surname, password) VALUES(?,?,?,?,?)"
    
    ## next registering the doctors
    cursor.execute(register_user_sql, [("MattyLee"), ("Matthew"), ("Lee"), ("9y24bkanbc"), ("D")])
    cursor.execute(register_user_sql, [("SuzieStoltz"), ("Suzanna"), ("Stoltz"), ("nl2jhiygsc"), ("D")])
    cursor.execute(register_user_sql, [("DWinehouse12"), ("Davida"), ("Winehouse"), ("bva572kac"), ("D")])

    ## committing changes to database
    db.commit()



    ## Tests
    cursor.execute("SELECT * FROM user ")
    assert(len(cursor.fetchall()))==9
    
    cursor.execute("SELECT username FROM user WHERE username='StewartSmith12'")
    assert(len(cursor.fetchall()))==1
