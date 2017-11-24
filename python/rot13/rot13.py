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

    def copy_file():
        name = sys.argv[1]
        rot13_name = "rot13_" + name

        read_file()
        copyfile(name, rot13_name)
        return rot13_name

    def switch_letter():
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        cap_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        for letter in read_file():
            if letter in alpha:
                x = alpha.index(letter)
                new_letter = letter.replace(letter, alpha[x + 13])
                rot13 = open(str(copy_file()), "w")
                rot13.write(new_letter)
            elif letter in cap_alpha:
                y = cap_alpha.index(letter)
                new_letter = letter.replace(letter, cap_alpha[y + 13])
                rot13 = open(str(copy_file()), "w")
                rot13.write(new_letter)


    switch_letter()

if __name__ == '__main__':
    main()


