# This is a simple implementation of the classic game Rock, Paper, Scissors.
# The player plays against the computer, and the game continues until the player decides to stop.
# The game includes input validation and handles invalid inputs gracefully.

import random

CHOICES = ["rock", "paper", "scissors"]
YES_RESPONSES = ["yes", "y"]

def main():
    print("Welcome to the Game of Rock, Paper, Scissors!")
    play_game()

def get_player_choice():
    invalid_count = 0
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice in CHOICES:
            return player_choice
        print("Invalid choice. Please try again.")
        
        invalid_count += 1
        if invalid_count > 2:
            continue_playing = input("You've entered invalid input several times. Do you still want to play? (yes/no): ").lower()
            if continue_playing not in YES_RESPONSES:
                print("Exiting the game.")
                exit()
            else:
                invalid_count = 0

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    while True:
        player_choice = get_player_choice()
        computer_choice = random.choice(CHOICES)
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in YES_RESPONSES:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()