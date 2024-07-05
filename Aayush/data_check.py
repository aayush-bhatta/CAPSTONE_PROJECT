import re

def email_validation(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print("Valid email")
    else:
        print("Invalid email.")
        raise ValueError

def number_check(number:int):
    string=str(number)
    if len(string)==10:
        print("Valid phone number.")
    else:
        print("Invalid phone number.")
        raise ValueError



