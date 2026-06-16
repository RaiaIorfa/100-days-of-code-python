import random
import hangman_art

print(hangman_art.hangman_arts[0])
print(f"************************WELCOME TO*****************************")
print(hangman_art.hangman_arts[1])

word_list = ["ardvark", "baboon", "camel"]
display = ""

chosen_word = random.choice(word_list)

for position in chosen_word:
    display += "_"

print(display + "\n")


lives = 6
gameover = False

while not gameover:
    user_guess = input("Guess a letter: ").lower()

    for index in range(0, len(chosen_word)):
        if user_guess == chosen_word[index]:
            display = display[:index] + user_guess + display[index + 1:]

    print(display)
    print(hangman_art.hangman_gallows[lives])
    
    if display == chosen_word:
        print("You've guessed the correct word. You win!!!")
        gameover = True