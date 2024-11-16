import random


def snack_game():
    snacks = ['chips', 'cookies', 'popcorn', 'candy', 'pres']
    random_snack = random.choice(snacks)

    guess = input("Guess the snack: ")

    if guess.lower() == random_snack:
        print("Congratulations! You guessed it right!")
    else:
        print("Oops! Wrong guess. The snack was", random_snack)


snack_game()
