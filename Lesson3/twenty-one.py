import os
import random

CARDS = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
SUITS = ["♦", "♥", "♣", "♠"]
VALUES = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
          "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
BLACKJACK = 21
DEALER_HITS = 17

def init_deck():
    deck = [str(card)+suit for card in CARDS
                           for suit in SUITS]
    return deck

def shuffle(deck):
    random.shuffle(deck)
    return deck

def hit(deck, hand):
    new_card = deck.pop()
    hand = set_hand(hand, new_card)
    return hand

def value(hand):
    hand_sum = sum([VALUES[card[:-1]] for card in hand["cards"]])
    ace_count = hand["ace_count"]

    while hand_sum > BLACKJACK:
        if ace_count > 0:
            ace_count -= 1
            hand_sum -= 10
        else:
            break

    return hand_sum

def set_hand(hand, new_card):
    if new_card[0] == "A":
        hand["ace_count"] += 1

    hand["cards"] += [new_card]
    hand["value"] = value(hand)

    return hand

def output_player_hand(hand):
    print(f"Your hand: {", ".join(sorted(hand["cards"]))}")
    print(f"Your total: {hand["value"]}")

def output_dealer_hand(hand):
    print(f"Dealer hand: {hand["cards"][0]}, ?")

def output_final_hand(p_hand, d_hand):
    output_player_hand(p_hand)
    print(f"Dealer hand: {", ".join(sorted(d_hand["cards"]))}")
    print(f"Dealer total: {d_hand["value"]}")

def twenty_one():
    os.system('clear')

    player_hand = {"ace_count":0, "cards": [], "value": 0 }
    dealer_hand = {"ace_count":0, "cards": [], "value": 0 }
    bust = False

    deck = init_deck()
    shuffle(deck)

    for _ in range(2):
        player_hand = hit(deck, player_hand)
        dealer_hand = hit(deck, dealer_hand)

    while True:
        output_player_hand(player_hand)
        output_dealer_hand(dealer_hand)
        play = input("Would you like to hit or stay? (h/s) : ")
        os.system('clear')


        if play.lower().startswith("h"):
            player_hand = hit(deck, player_hand)

            if player_hand["value"] > BLACKJACK:
                bust = True
                print("Player Bust - You Lose")
                output_final_hand(player_hand, dealer_hand)
                break
        else:
            break

    while not bust:
        if dealer_hand["value"] < DEALER_HITS:
            dealer_hand = hit(deck, dealer_hand)
            if dealer_hand["value"] > BLACKJACK:
                bust = True
                print("Dealer Bust - You Win")
                output_final_hand(player_hand, dealer_hand)
                break
        else:
            break


    if player_hand["value"] > dealer_hand["value"] and not bust:
        output_final_hand(player_hand, dealer_hand)
        print("Closer to 21 - You Win!")
    elif player_hand["value"] == dealer_hand["value"] and not bust:
        output_final_hand(player_hand, dealer_hand)
        print("Tie - No Winner!")
    elif not bust:
        output_final_hand(player_hand, dealer_hand)
        print("Dealer Wins!")

while True:
    twenty_one()
    replay = input("Would you like to play again? (y/n): ")
    if not replay.lower().startswith("y"):
        break
