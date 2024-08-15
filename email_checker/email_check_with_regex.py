import re

check_email="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_Email=input("Enter your email : ")

if re.search(check_email,user_Email):
    print("Right email")
else:
    print("wrong email")