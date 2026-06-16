from rock_paper_scissors import RockPaperScissors

game = RockPaperScissors()

continue_game = True

while continue_game:
    game.game_start()
    go_again = input("Do you want to play again? 'y' or 'n': ").lower()
    if go_again != 'y':
        continue_game = False
        print("Goodbye, see you again👋")
    else:
        game.computer_score = 0
        game.player_score = 0