import random
import os
from art import *

def deal_card(user_cards, dealer_cards, cards, count=1, user=False, dealer=False):
    if dealer:
        dealer_cards.append(random.choice(cards))
    elif user:
        user_cards.append(random.choice(cards))
    else:
        for _ in range(count):
            user_cards.append(random.choice(cards))
            dealer_cards.append(random.choice(cards))

def reveal_hand(user_cards, dealer_cards, uscore, dscore):
    """
    Reveals the cards drawn by the user and dealer, and displays the sum respectively.
    """
    print(f"Your cards: {user_cards}  sum: [{uscore}]")
    print(f"Dealers cards: {dealer_cards}  sum: [{dscore}]")    

def open_dispay(u_display_cards, d_display_cards, u_display_score):
    os.system('cls' if os.name == 'nt' else 'clear') # Cross-platform clear screen
    print(logo[0])
    print(f"Your cards: {u_display_cards} (Current score: {u_display_score})")
    print(f"Dealers first card: [{d_display_cards[0]}]")

def soft_hand(checked_cards):
    """
    Adjusts the value of the Ace from 11 to 1 if the total score exceeds 21.
    """
    while sum(checked_cards) > 21 and 11 in checked_cards:
        checked_cards.remove(11)
        checked_cards.append(1)
        # return checked_cards

def blackjack():
    cards = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    user_cards = []
    dealer_cards = []

    deal_card(user_cards, dealer_cards, cards, count=2)

    # -----------PLAYER'S TURN-------------
    while True:
        user_score = sum(user_cards)
        dealer_score = sum(dealer_cards)
        open_dispay(user_cards, dealer_cards, user_score)

        # TODO: Check if user has blackjack or if the dealer has blackjack, and handle the game outcome accordingly.
        if user_score == 21 and dealer_score == 21 and len(user_cards) == 2 and len(dealer_cards) == 2:
            reveal_hand(user_cards, dealer_cards, user_score, dealer_score)
            print("Push! Both you and the dealer have Blackjack!")
            return
        elif dealer_score == 21 and len(dealer_cards) == 2:
            reveal_hand(user_cards, dealer_cards, user_score, dealer_score)
            print("Dealer got Blackjack! You Lose!")
            return
        elif user_score == 21 and len(user_cards) == 2:
            reveal_hand(user_cards, dealer_cards, user_score, dealer_score)
            print("Blackjack! You win!")
            return

        # Prompt player to Hit or Stand
        deal_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if deal_again == 'y':
            deal_card(user_cards, dealer_cards, cards, count=1, user=True)
            soft_hand(user_cards)
            user_score = sum(user_cards)
            if user_score > 21:
                reveal_hand(user_cards, dealer_cards, user_score, dealer_score)
                print("Bust! You Lose!")
                return
            open_dispay(user_cards, dealer_cards, user_score)
        else:
            break

    # ----------DEALER'S TURN-------------    
    while dealer_score < 17:
        deal_card(user_cards, dealer_cards, cards, count=1, dealer=True)
        soft_hand(dealer_cards)
        dealer_score = sum(dealer_cards) 
        if dealer_score > 21:
            reveal_hand(user_cards, dealer_cards, user_score, dealer_score)
            print("Dealer Busts! You Win!")
            return
            
    # ----------CHECKING WINNER-------------
    if user_score == dealer_score:
        reveal_hand(user_cards, dealer_cards, user_score, dealer_score)
        print("Push! Both you and the dealer have equal score.")
    elif user_score > dealer_score:
        reveal_hand(user_cards, dealer_cards, user_score, dealer_score)
        print("You Win!")
    else:
        reveal_hand(user_cards, dealer_cards, user_score, dealer_score)
        print("You Lose!")

choice = input("Welcome to Blackjack! Press 'y' to play or 'n' to quit: ").lower()
if choice == 'y':
    blackjack()

play_again = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
while play_again == 'y':
    blackjack()
    play_again = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()