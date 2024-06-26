#Prompt the user to create a password. If the passwords do not match the user will have to create a password again
import random

def create_password():
    user_password=input("Create your password ")
    confirm_password=input("Confirm your password ")
    if user_password==confirm_password:
        return user_password
    else:
        return "Passwords dont match. Try again"


capital_letters="WERTYUIOPASDFGHJKLZXCVBNM"
lowercase_letters="qwertyuiopasdfghjklzxcvbnm"
integer="1234567890"
special_characters="!@#$%^&*()_+=|\{}[]:;,./<>?"
upper,lower,digits,odd=True,True,True,True

charactersinpassword=""
if upper:
    charactersinpassword+=capital_letters
if lower:
    charactersinpassword+=lowercase_letters
if digits:
    charactersinpassword+=integer
if odd:
    charactersinpassword+=special_characters

howmanypasswords=1

for z in range(howmanypasswords):
    new_password=create_password()
    print(f"Your new password is {new_password}")
