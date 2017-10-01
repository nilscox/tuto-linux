import random

SECRET_LIST = [
    "diplodocus",
    "avion",
    "justice",
    "bureau",
    "pasteque",
    "mathematique",
    "aventure",
    "consoles",
    "dictionnaire",
    "histoire",
    "estomac",
    "baignoire",
    "parapluie",
    "sauvage",
    "amour",
    "bisous",
    "sphynx",
    "canard",
]

secret_word = None
lives = 0
tab = []


def start(bot, args):
    global secret_word
    global lives
    global tab

    if len(args) < 1:
        return "You must provide a channel."

    channel = args[0]

    lives = 11
    tab = []

    if len(args) > 1:
        secret_word = args[1]
    else:
        secret_word = random.choice(SECRET_LIST)

    bot.send_message(channel, "*" * len(secret_word))

    return "The game just started."


def answer(args):
    global secret_word
    global lives
    global tab

    letter = args[1].lower()

    if letter is None or len(letter) != 1:
        return "You must answer a letter."

    if lives == 0:
        return "You're hanged, man!"

    tab.append(letter)

    result = ""

    for l in secret_word:
        if l in tab:
            result += l
        else:
            result += "*"

    if letter not in secret_word:
        lives -= 1

    if lives == 0:
        return "You're hanged, man! The answer was: " + secret_word

    return "Lives : " + str(lives) + ", " + result


def hangman(bot, args):
    command = args[0]

    if command == "start":
        return start(bot, args[1:])
    elif command == "answer":
        return answer(args)
    else:
        return "You must enter 'start' if you want to begin or 'answer' if you want to continue."
