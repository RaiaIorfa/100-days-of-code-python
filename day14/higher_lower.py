import random
import os
from art import logo
from game_data import game_data

def format_account(account):
    """Formats the account data into a clean printable string format."""
    return f"{account['name']}, a {account['description']}, from {account['country']}."

def check_answer(guess, a_followers, b_followers):
    """
    Checks the user's guess against follower counts.
    Returns True if correct (including ties), False if wrong.
    """
    if a_followers > b_followers:
        return guess == "A"
    elif b_followers > a_followers:
        return guess == "B"
    else:
        # If there is a tie, any guess 'A' or 'B' is considered acceptable/safe
        return guess in ["A", "B"]

def play_higher_lower():
    score = 0
    game_over = False
    
    # Select our initial starting account
    account_a = random.choice(game_data)
    
    while not game_over:
        # Get a new account for B and ensure it's never identical to A
        account_b = random.choice(game_data)
        while account_a == account_b:
            account_b = random.choice(game_data)
            
        # UI Refresh
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo[1])
        
        if score > 0:
            print(f"You're right! Current score: {score}")
            
        print(f"Compare A: {format_account(account_a)}")
        print(logo[3])
        print(f"Against B: {format_account(account_b)}")
        
        # Input validation loop
        user_choice = ""
        while user_choice not in ["A", "B"]:
            user_choice = input("Who's more popular? Type 'A' or 'B': ").upper()

        # Extract values for the evaluation
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        
        # Check if the player is right
        if check_answer(user_choice, a_followers, b_followers):
            score += 1
            account_a = account_b  # B becomes the new A for the next round
        else:
            # End Game sequence
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo[1])
            print(f"Oops, that's wrong. Final score: {score}")
            game_over = True

# Main Execution Guard
if __name__ == "__main__":
    playing = True
    while playing:
        play_higher_lower()
        print("-" * 40)
        play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if play_again != 'y':
            playing = False
            print("Thanks for playing! Goodbye.")