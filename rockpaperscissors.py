

import random
def playRockPaperScissors():
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    user_choice = input("Enter selection (rock/paper/scissors): ")
    print(f"Computer choice: {computer_choice}")
    if user_choice.lower() == computer_choice:
        return "Tie game"
    elif user_choice.lower() == "rock":
        if computer_choice == "scissors":
            return "user"
        else:
            return "computer"
    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            return "user"
        else:
            return "computer"
    elif user_choice.lower() == "scissors":
        if computer_choice == "paper":
            return "user"
        else:
            return "computer"
    else:
        print("Invalid choice")
        
num_rounds = 0
user_wins = 0
computer_wins = 0
play_again = "y"

while play_again.lower() == "y":
    num_rounds += 1
    result = playRockPaperScissors()
    if result == "user":
        user_wins += 1
        print("You win!")
    elif result == "computer":
        computer_wins +=1
        print("Computer wins!")
    else:
        print("Tie game")
    print(f"Rounds played: {num_rounds}")
    print(f"Computer wins: {computer_wins}")
    print(f"User wins: {user_wins}")
    play_again = input("play another round (y/n): ")
    
    if play_again == "n":
        print("Game has been ended")