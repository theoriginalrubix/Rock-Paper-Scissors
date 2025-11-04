import random

while True:
    user_action = input("Enter a Choice (Rock, Paper, Scissors): ").capitalize() 
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions) 

    print(f"\nYou Chose {user_action}, Computer Chose {computer_action}\n")
    
    if user_action == computer_action:
        print(f"Both Players Selected {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock Smashes Scissors! You Win!")
        else:
            print("Paper Covers Rock! You Lose.")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper Covers Rock! You Win!")
        else:
            print("Scissors Cuts Paper! You Lose.")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors Cut Paper! You Win!")
        else:
            print("Rock Smashes Scissors! You Lose.")
            
    play_again = input("Play Again? (Y/N): ")
    if play_again.lower() != "y":
        break