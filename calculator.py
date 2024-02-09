import sys

'''TASK 2

Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.

Perform the calculation and display the result.'''
def first_num():
    """Prompt user to enter the first number of their  equation, and gives them the chance to exit the programme"""

    while True:
        number1 =  input("What is your first number ")
        if number1.isdigit():
            return int(number1)
        elif number1 == "off" : 
            switch()
        else:
            print("Invalid input, please enter only digits.")


def second_num():
    """Prompt user to enter the second number of their  equation, and gives them the chance to exit the programme"""
    while True:
        number2 = input("What is your second number ")
        if number2.isdigit():
            return int(number2)
        elif number2 == "off": 
            switch()
        else:
            print("Invalid input, please enter only digits.")


def switch():
    """This function exits the programme at any given point, once a user enters off"""
    print("Goodbye")
    sys.exit()

def sign():
    """THis function gets input from the  user for which mathematical operation they want to perform."""
        
    while True:
        sign = input("""
    Which mathematical symbol would you like to use
    additional (+)
    subtraction (-)
    multiplication (*)
    division (/)              
    > """)

        if sign in ['+', '-', '*', '/']:
            return sign
        elif  sign.lower() == "off":
            switch()
        else:
            print("""The only commands the calculator recognises is as follows
additional (+)
subtraction (-)
multiplication (*)
division (/)
              """)

            
def calculator(sign, number1, number2):
    """The calculator runs the main part of the programme taking in the sign, number2 and number2 as arguments"""
    if sign == "+":
        return sum(number1, number2)
    elif sign == "-":
        return minus(number1 , number2)
    elif sign == "*":
        return multiplication(number1, number2)
    elif sign == "/":
        return division(number1, number2)
    else:
        print("Symbol choosen is invalid or incorrect")

    print(f" THIS IS THE OPERATOR USED {sign}")

def sum(num1, num2):
    """Runs the + operator and displays the results"""
    result = num1 + num2
    print(f"The addition of {num1} and {num2} is {result}")
    return result
    #return num1 + num2

def minus(num1, num2):
    """Runs the - operator and displays the results"""
    result = (num1 -  num2)
    print(f"The subtraction of {num1} and {num2} is {result}")
    return result

def multiplication(num1, num2):
    """Runs the  * operator and displays the results"""
    result = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {result}")
    return result

def division(num1, num2):
    """Runs the / operator and handles exceptions for division by zero and non-integer arguments."""
    if num2 == 0:
        print("zero can not be a denominator for division purposes.")
        return None
    result = (num1 / num2)
    print(f"The division of {num1} and {num2} is {result}")
    return result

if __name__ == "__main__":
    print("Welcome to your personal standard computer")

    while True:
        number1 = first_num()
        number2 = second_num()
        operator = sign()
        result = calculator(operator,  number1, number2)
        
        continuing = input("Would you want to perform another calculation? Type yes or no\n").lower().strip()
        if continuing == 'yes':
            continue
        elif continuing == "no":
            switch()
            break
