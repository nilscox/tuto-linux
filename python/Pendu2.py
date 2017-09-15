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
    return l not in secret_word


def win(lives, tab, secret_word):
    if lives == 0:
        return False

    for letter in secret_word:
        if letter not in tab:
            return False

    return True


def game():
    secret_word = input("Enter your secret word: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    tab = []
    lives = 11

    while lives > 0 and not win(lives, tab, secret_word):
        if turn(tab, secret_word):
            lives -= 1

        print(lives)

    if win(lives, tab, secret_word):
        print("You win!")
    else:
        print("You didn't win this time x(")

game()
