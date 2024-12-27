# Rock , Paper, Scissors
import random

def game():
    usrChoice = input("\033[1;33m r for rock \033[0m,\033[1;36m s for scissors \033[0m,\033[1;33m p for paper \033[0m \033[5mEnter your choice:\033[0m ").lower()# Ask the user for their choice
    # I'm using the escape codes for enhancements you can use the below line as well
    # usrChoice = input(" r for rock, p for papers, s for scissors, What's your choice? ")
    
    # Validate user input
    if usrChoice not in ["r", "p", "s"]:
        return "\033[31mInvalid input. Please enter 'r', 'p', or 's'.\033[0m"
    
    computerChoice = random.choice(["r", "p", "s"]) 
    
    # Display the computer's choice
    print(f"Computer's choice: \033[1;34m{computerChoice}\033[0m")

    # If it's a tie
    if usrChoice == computerChoice:
        return "It's a tie 🟰"

    # Check if the user wins
    if usr_win(usrChoice, computerChoice):# you can change the parametres when you need to take output from any other variables so in this case i changed them from the default ones
        return "Hey! You \033[5mwon\033[0m 🎉"#again the escape codes are just for enhancing appearance!!!

    return "Ah sorry! You \033[5mlost\033[0m 😞"


def usr_win(user, computer):
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True
    return False

print(game())#calling the function or just say printing the function