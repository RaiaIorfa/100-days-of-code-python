# import random

# rock = "🪨"
# paper = "📄"
# scissors = "✂️"

# print("Welcome to Rock, Paper, Scissors!\n")
# user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# if user_choice == 0:
#     user_choice = "rock"
# elif user_choice == 1:
#     user_choice = "paper"
# elif user_choice == 2:
#     user_choice = "scissors"
# else:
#     print("wrong input!")

# computer_options = ["rock", "paper", "scissors"]
# computer_choice = random.choice(computer_options)

# if computer_choice == "rock":
#     ce = rock
# elif computer_choice == "paper":
#     ce = paper
# elif computer_choice == "scissors":
#     ce = scissors

# if user_choice == "rock":
#     ue = rock
# elif user_choice == "paper":
#     ue = paper
# elif user_choice == "scissors":
#     ue = scissors

# if computer_choice == user_choice:
#     print(f"computer choose {ce} and you choose {ue}. It's a draw ")
# elif user_choice == "rock" and computer_choice == "scissors":
#     print(f"computer choose {ce} and you choose {ue}. You won! ")
# elif user_choice == "paper" and computer_choice == "rock":
#     print(f"computer choose {ce} and you choose {ue}. You won! ")
# elif user_choice == "scissors" and computer_choice == "paper":
#     print(f"computer choose {ce} and you choose {ue}. You won! ")
# else:
#     print(f"computer choose {ce} and you choose {ue}. Computer won! ")


# ------------------Version 2---------------------- 

import random

def rock_paper_scissors():
    game_choices = {
        "rock": "🪨 ",
        "paper": "📄 ",
        "scissors": "✂️ "
    }
    game_over = False
    scores = {
        "computer": 0,
        "user": 0
    }
    while not game_over:  
        dash = "_" * 50          
        valid_inuput = False
        while not valid_inuput:
            user_choice = input("Type 'rock', 'paper', 'scissors': ").lower()
            # wrong input check
            if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
                valid_inuput = True
            else:
                print("❌ Wrong input!")

        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        if computer_choice == user_choice:
            print(f"computer choose {game_choices[computer_choice]} and you choose {game_choices[user_choice]}. This round is a draw.")
            print(f"Player: {scores['user']} | Computer: {scores['computer']}\n{dash}")
        elif user_choice == "rock" and computer_choice == "scissors":
            print(f"computer choose {game_choices[computer_choice]} and you choose {game_choices[user_choice]}. You won this round!")
            scores["user"] += 1
            print(f"Player: {scores['user']} | Computer: {scores['computer']}\n{dash}")
        elif user_choice == "paper" and computer_choice == "rock":
            print(f"computer choose {game_choices[computer_choice]} and you choose {game_choices[user_choice]}. You won this round!")
            scores["user"] += 1
            print(f"Player: {scores['user']} | Computer: {scores['computer']}\n{dash}")
        elif user_choice == "scissors" and computer_choice == "paper":
            print(f"computer choose {game_choices[computer_choice]} and you choose {game_choices[user_choice]}. You won this round!")
            scores["user"] += 1
            print(f"Player: {scores['user']} | Computer: {scores['computer']}\n{dash}")
        else:
            print(f"computer choose {game_choices[computer_choice]} and you choose {game_choices[user_choice]}. Computer won this round!")
            scores["computer"] += 1
            print(f"Player: {scores['user']} | Computer: {scores['computer']}\n{dash}")

        if scores["computer"] == 3 or scores["user"] == 3:
            game_over = True
            print("Scores:")
            print(f"Player: {scores['user']} | Computer: {scores['computer']}\n{dash}")
            if scores["computer"] > scores["user"]:
                print("COMPUTER WINS!")
            else:
                print("YOU WIN!")

print("Welcome to Rock, Paper, Scissors!\n")

rock_paper_scissors()