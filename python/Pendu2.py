import os


def turn(tab, secret_word):
    l = input("Enter a letter : ").lower()

    if l not in tab:
            tab.append(l)
    else:
        turn(tab, secret_word)


    print("\n", tab, "\n")

    for letter in secret_word:
            if letter in tab:
                print(letter, end=" ")
            else:
                print("*", end=" ")

    print("\n")
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

        print("lives : ", str(lives) + "\n")

    if win(lives, tab, secret_word):
        print("You win!")
    else:
        print("You didn't win this time x(")

game()
