import random
import os
from art import logo

class NumberGuessGame():
    # self.difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    DIFFICULTY = {
        "easy": 10,
        "hard": 5
    }

    def __init__(self):
        self.attempts = 0
        self.random_num = 0
        self.validate_input(diffculty)

    def choose_difficulty(self, difficulty):
        if difficulty == "easy":
            self.attempts = self.DIFFICULTY["easy"]
        elif difficulty == "hard":
            self.attempts = self.DIFFICULTY["hard"]
    
    def validate_input(self, diffculty):
        if diffculty != "easy" or diffculty != "hard":
            return False
    
    def gen_rand_int(self):
        self.random_num = random.randint(1, 100)

    def display_welcome_screen(self):
        os.system('cls')
        print(logo[0])
        print("WELCOME TO THE NUMBER GUESSING GAME!")
        print("I'm thinking of a number between 1 and 100. Guess\n🤖 ...")




def num_guess():
    rand_num = random.randint(1, 100)
    error = ""

    while True:
        os.system('cls')
        print(logo[0])
        print("WELCOME TO THE NUMBER GUESSING GAME!")
        print("I'm thinking of a number between 1 and 100. Guess\n🤖 ...")
        if error:
            print(f"❌ {error}")
        
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            attempts = 10
            break
        elif difficulty == 'hard':
            attempts = 5
            break
        else:
            error = "Invalid input! Please choose 'easy' or 'hard'.\n"
    
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess > rand_num:
            print("🤖 Too high. Try again.")
            attempts -= 1
            print(f"⚠️  You have {attempts} attempts left\n")
        elif guess < rand_num:
            print("🤖 Too low. Try again.")
            attempts -= 1
            print(f"⚠️  You have {attempts} attempts left\n")
        elif guess == rand_num:
            print("🤖 Wow you got it! You win🎉\n")
            break
    
    if attempts == 0:
        print(f"🤖 You ran out of guesses. You Lose \n The answer is {rand_num}")

num_guess()

play_again = input("Do you want to play again? 'y' or 'n': ").lower()

while play_again == 'y':
    num_guess()
    play_again = input("Do you want to play again? 'y' or 'n': ").lower()
