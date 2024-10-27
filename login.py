import json
import re

def login():
    try:
        with open("user_data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("File not found, please register first")
        return
    
    while True:
        emai = input("enter your email ")
        passwo = input("enter your password ")

        if data.get("email") == emai and data.get("password") == passwo:
            print("Login successful")
            break
        else:
            print("Login Failed, please check your email and password")



def emailvalid():
    pattern = r"^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}(\.[a-zA-Z]{2,6})?$"
    vali = True
    while True:
        email = input("What is your email address? ") if vali else input("Invalid email format, please re-enter it: ")
        if re.search(pattern, email):
            print("Valid email")
            return email
            
        else:
            vali = False
            


def passwordvalid():
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*+?])(?=.*\d)[a-zA-Z0-9!@#$%^&*?~]{8,}$"
    valid = True
    while True:       
        passw = input("Now create your password: ") if valid else input("The password doesn't meet the requirements, please re-enter it again: ")
        if re.search(pattern, passw):
            print("Valid Password")
            return passw
        else:
        
            valid = False
            
    
def phonenum():
    pattern = r"^(\+?\d{1,3}[ .-]?)?(\(?\d{3}\)?[ .-]?)\d{3}[ .-]?\d{4}$"
    val = True
    while True:
        number = input("What is your phone number? ") if val else input("Invalid phone number, please re-enter it")
        if re.search(pattern, number):
            print("Valid Phone number")
            return number
        else:
            val = False



