import re 
import json
from login import emailvalid, passwordvalid, phonenum, login




email = emailvalid()
password = passwordvalid()
number = phonenum()

data = {"email": email, "password": password, "Phone": number}

with open("user_data.json", "w") as file:
    json.dump(data, file)

