"""
A password generator is a useful tool that generates strong and

random passwords for users. This project aims to create a
password generator application using Python, allowing users to

specify the length and complexity of the password.

User Input: Prompt the user to specify the desired length of the

password.

Generate Password: Use a combination of random characters to

generate a password of the specified length.

Display the Password: Print the generated password on the screen."""
import random 
import string
import sys

def  leng_password():
    while True:
        try:
            password_len = int(input("Password length "))
            return password_len
        except ValueError:
            print("You have to enter the length of the password you want to generate, NO  alphabets or special characters are allowed.")
            continue

def complexity(length):
   # while True:
        try:
            pass_complexity = input("The complexity for a generated password is: 1.Strong 2. Medium 3. Weak ").strip().lower()
            if  pass_complexity == '1': # or pass_complexity == "strong":
                strong(length)
            elif  pass_complexity == '2' or pass_complexity == "medium" :
                medium(length)
            elif   pass_complexity == '3' or pass_complexity == "weak":
                weak(length)
            elif pass_complexity == "exit":
                off()

        except ValueError:
           print("Your complexity input is invalid, please try again")


def strong(length):
    """The strong complexity generator will generate a password with alphabets, numericals and specisl characters"""
    strong_password = ''
    for _ in range(length):
        determiner = string.ascii_letters + string.digits + string.punctuation
        strong_password += random.choice(determiner)
    print(f"The strong password generated is {strong_password}")
    return strong_password

def medium(length):
    "The medium complexity generator will generate only alphabets and numbers"
    medium_password = ''
    for _  in range(length):
        determiner = string.ascii_letters + string.digits
        medium_password += random.choice(determiner)
    print(f"The medium password generated is {medium_password}")

def  weak(length):
    """The weak complexity generator will only generate alphabets"""
    #ascii_letters
    weak_password = " "
    for _ in range(length):
        determiner = string.ascii_letters
        weak_password += random.choice(determiner)
    print(f"The weak password generated is {weak_password}")
    return weak_password


def off():
    print("Goodbye")
    sys.exit()


if __name__ == "__main__":
   password_len = leng_password()
   complexity_ = complexity(password_len)
