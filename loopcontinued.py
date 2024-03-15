import random

cards = ["Hearts", "Spades", "Clubs", "Diamonds"]
for card in range(5):
    random.shuffle(cards)
    print(cards)


    # deck_shuffle = random.shuffle(cards)
    # if deck_shuffle < 5:
    #     print(deck_shuffle)