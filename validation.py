def input_valid_bool(data):
    value = input(f"Enter Y if the patient has {data} and N if they do not: ".format(data=data))
    while True:
        if value in ["Y", "N"]:
            return value
        else:
            print("Error input should be either Y or N. Please try again")
            value = input(f"Enter Y if the patient has {data} and N if they do not: ".format(data=data))

def input_specific_char(data, accepted_chars):
    prompt = f"Enter the patient's {data} [".format(data=data)
    for char, description in accepted_chars.items():
        prompt += char + ": "+ description + ", "
    char = input(prompt[:-2]+"]")
    
    while True:
        chars = list(accepted_chars.keys())
        if char in chars:
            return char
        else:
            print("Error input should be in {values}. Please try again".format(values=chars))
            char = input(prompt)

def input_valid_integer(data):
    value = input(f"Enter the patient's {data} as an integer".format(data=data))
    while True:
        try:
            value = int(value)
            return value
        except ValueError:
            print(f"Error {data} should be an integer. Please try again".format(data=data))
            value = input(f"Enter the patient's {data} as an integer".format(data=data))

def input_valid_range(data, min_value, max_value):
    value = input(f"Enter the patient's {data} as an integer".format(data=data))
    while True:
        try:
            value = int(value)
            if value not in range(min_value, max_value):
                raise ValueError
            return value
        except ValueError:
            print(f"Error {data} should be an integer between {min_value} and {max_value}. Please try again".format(data=data, max_value=max_value, min_value=min_value))
            value = input(f"Enter the patient's  {data} as an integer between {min_value} and {max_value}".format(data=data, max_value=max_value, min_value=min_value))

def input_valid_float(data):
    value = input(f"Enter the patient's  {data} as an float".format(data=data))
    while True:
        try:
            value = float(value)
            return value
        except ValueError:
            print(f"Error {data} should be an float. Please try again".format(data=data))
            value = input(f"Enter the patient's {data} as an float".format(data=data))


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
