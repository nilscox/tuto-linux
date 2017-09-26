import random


SECRET_LIST = ["diplodocus","avion","justice","bureau","pasteque",
                    "mathematique","aventure","consoles","dictionnaire","histoire",
                    "estomac","baignoire", "parapluie", "sauvage", "amour", "bisous", "sphynx", "canard"

]


class Hangman:

    def __init__(self):
        self.secret_word = ""
        self.lives = 0
        self.tab = []

    def start(self, args):
        self.secret_word = random.choice(SECRET_LIST)
        self.lives = 11
        self.tab = []
        return "*" * len(self.secret_word)

    def answer(self, args):
        letter = args[1].lower()

        if letter is None or len(letter) != 1:
            return "You must answer a letter."

        if self.lives == 0:
            return "You're hanged, man!"

        self.tab.append(letter)

        result = ""

        for l in self.secret_word:
            if l in self.tab:
                result += l
            else:
                result += "*"

        if letter not in self.secret_word:
            self.lives -= 1

        if self.lives == 0:
            return "You're hanged, man! The answer was: " + self.secret_word

        return "Lives : " + str(self.lives) + ", " + result

    def command(self, args):
        command = args[0]

        if command == "start":
            return self.start(args)
        elif command == "answer":
            return self.answer(args)
        else:
            return "You must enter 'start' if you want to begin or 'answer' if you want to continue."
