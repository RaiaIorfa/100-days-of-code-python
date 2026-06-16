import random
import os

class RockPaperScissors:
    def __init__(self):
        self.GAME_CHOICES = {
            "rock": "🪨 ",
            "paper": "📄 ",
            "scissors": "✂️ "
        }
        # A simple map showing what each choice beats
        self.WINNING_RULES = {
            "rock": "scissors",  # Rock beats scissors
            "paper": "rock",      # Paper beats rock
            "scissors": "paper"   # Scissors beats paper
        }
        self.computer_score = 0
        self.player_score = 0
        self.computer_choice = ""
        self.player_choice = ""
    
    def game_start(self):
        os.system("cls")
        print("Welcome to Rock, Paper, Scissors! First to 3 wins.")
        
        while self.computer_score < 3 and self.player_score < 3:            
            self.computer_choice = random.choice(list(self.GAME_CHOICES.keys()))
            
            # Keep asking until input is valid
            user_input = input("Type 'rock', 'paper', 'scissors': ").lower()
            while not self.is_valid_input(user_input):
                user_input = input("❌ Invalid choice. Type 'rock', 'paper', or 'scissors': ").lower()
            
            # Explicitly set state after validation passes
            self.player_choice = user_input

            self.evaluate_round()
            self.display_score()

        # Check final game status
        if self.player_score == 3:
            print("\n🎉 CONGRATULATIONS! YOU WIN THE GAME! 🎉")
        else:
            print("\n💻 GAME OVER! COMPUTER WINS THE GAME! 💻")

    def is_valid_input(self, u_input):
        """Pure validation check method."""
        return u_input in self.GAME_CHOICES
    
    def display_score(self):
        print(f"You chose {self.GAME_CHOICES[self.player_choice]} vs Computer {self.GAME_CHOICES[self.computer_choice]}")
        print(f"Scoreboard -> Player: {self.player_score} | Computer: {self.computer_score}")
        print("_" * 50 + "\n")

    def evaluate_round(self):
        """Evaluates round score rules using dictionary relationships."""
        if self.player_choice == self.computer_choice:
            print("This round is a draw!")
        elif self.WINNING_RULES[self.player_choice] == self.computer_choice:
            print("You won this round!")
            self.player_score += 1
        else:
            print("Computer won this round!")
            self.computer_score += 1

# Driver initialization code
if __name__ == "__main__":
    game = RockPaperScissors()
    game.game_start()
