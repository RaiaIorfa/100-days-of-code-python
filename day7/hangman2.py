import random
import hangman_art
from hangman_words import word_lists

print(hangman_art.hangman_arts[0])
print(f"************************WELCOME TO*****************************")
print(hangman_art.hangman_arts[1])

placeholder = ""

chosen_word = random.choice(word_lists)
correct_letters = []

for position in chosen_word:
    placeholder += "_"

print(placeholder + "\n")

lives = 6
gameover = False

while not gameover:
    print(f"******************************************** {lives}/6 LIVES LEFT ********************************************")
    user_guess = input("Guess a letter: ").lower()
    display = ""

    if user_guess in correct_letters:
        print(f"You've already guessed letter [{user_guess}]")        

    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if user_guess in chosen_word:
        print(display)
        print(hangman_art.hangman_gallows[lives])
    else:
        lives -= 1
        print(display)
        print(f"[{user_guess}] is not in the hidden word. You lose a life")
        print(hangman_art.hangman_gallows[lives])

    if display == chosen_word:
        gameover = True
        print("You've guessed the correct word. YOU WIN!!!")
    elif lives == 0:
        gameover = True
        print(f"{hangman_art[2]} \n IT WAS {chosen_word}. YOU LOSE!!!!!")