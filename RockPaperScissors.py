import random
import sys

def  get_user_choice():

    while True:
        user_selection = input("""
        Select a hand to play:
        Rock
        Paper
        Scissors
        You can also switch off the game
            
            > """).lower()
        if user_selection == "off":
            switch()
        elif user_selection == "paper" or user_selection == "rock" or user_selection == "scissors":
            print(f"You have selected {user_selection} as your handle.")
        else:
            print(f"I do not understand {user_selection}.")
            continue
            
        return user_selection
    
def switch():
    print("""\n Game over, goodbye!""")
    sys.exit()


def get_computer_selection():

    valid_selection = ("rock", "paper", "scissor")
    computer_selection = random.choice(valid_selection)

    print(f"The computer has randomly choosen {computer_selection}.")
    return computer_selection

def main_game(user_input, computer_choice):
    if user_input == computer_choice:
        return print(f"""
USER {user_input}
COMPUTER {computer_choice}
RESULT : It's a tie!
""")
    elif (user_input == "scissor" and computer_choice == "paper") or \
         (user_input == "rock" and computer_choice == "scissor") or \
         (user_input == "paper" and computer_choice == "rock"):

        return print(f"""
USER : {user_input}
COMPUTER : {computer_choice}
RESULTING : User wins""")
    
    else:
        return print(f"""
USER : {user_input}
COMPUTER : {computer_choice}
RESULTING : You lose!""")
    
    
if __name__ == "__main__":
    print("Welcome to Rock-PAper-Scissor GAme!\n")

    while True:
        user_input = get_user_choice()
        if user_input == "off":
            switch()
        else:
            computer_choice = get_computer_selection()
            main_game(user_input, computer_choice)
            