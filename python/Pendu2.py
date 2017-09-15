import os


def turn(tab, secret_word):
    l = input("Enter a letter : ").lower()
    tab.append(l)

    for letter in secret_word:
            if letter in tab:
                print(letter, end=" ")
            else:
                print("*", end=" ")

    print()
    return False


def win(lives, tab, secret_word):
    if lives == 0:
        return False

    for letter in secret_word:
        if letter not in tab:
            return False



def game():
    secret_word = input("Enter your secret word: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    tab = []
    lives = 11

    while not win(lives, tab, secret_word):
        turn(tab, secret_word)

    print("You win!")


game()
