import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one: (1) Rock, (2) Paper, (3) Scissors")
    user_choice = int(input("Enter your choice: "))
    
    if user_choice not in [1, 2, 3]:
        print("Invalid choice. Please try again.")
        return
    
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.randint(1, 3)
    
    print("You chose:", choices[user_choice-1])
    print("Computer chose:", choices[computer_choice-1])
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")

play_game()
