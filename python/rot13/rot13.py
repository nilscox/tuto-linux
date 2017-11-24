import sys
import os
from shutil import copyfile


def main():

    def read_file():

        if not os.path.isfile(sys.argv[1]):
            print('There is no file name ', sys.argv[1])
            sys.exit(1)

        file = open(sys.argv[1], 'r+')
        while True:
            letter = file.read(1)
            file.close()
            return letter


    def switch_letter(letter):
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#        cap_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        name = sys.argv[1]
        rot13_name = "rot13" + name

        read_file()
        copyfile(name, rot13_name)

        x = alpha.index(letter)
#        y = cap_alpha.index(letter)

        if letter in alpha:
            letter.replace(letter, alpha[x + 13])
 #       elif letter in cap_alpha:
#           letter.replace(letter, cap_alpha[y + 13])

        print(letter.replace(letter, alpha[x + 13]))

    switch_letter("a")

if __name__ == '__main__':
    main()