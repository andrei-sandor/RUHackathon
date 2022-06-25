with sqlite3.connect("UserData.db") as db:
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    username VARCHAR(20) PRIMARY KEY,
    firstname VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    user_type CHAR NOT NULL);
    ''')

    # check following datatypes are correct
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
    oldpeak VARCHAR(10) NOT NULL,,
    stSlope VARCHAR(4) NOT NULL,
    username VARCHAR(20) PRIMARY KEY,
    FOREIGN KEY(username) REFERENCES user(username));
    ''')
