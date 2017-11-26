import sys
import os
import re


def rot13(letter):
    if not ('A' <= letter <= 'Z' or 'a' <= letter <= 'z'):
        return letter
    else:
        if letter.isupper():
            letter_place = ord(letter) - ord('A')
            new_letter_place = (letter_place + 13) % 26
            return chr(new_letter_place + ord('A'))
        else:
            letter_place = ord(letter) - ord('a')
            new_letter_place = (letter_place + 13) % 26
            return chr(new_letter_place + ord('a'))


def get_new_file_name(old_file_name):
    match = re.match(r"((.+)\.rot13)", old_file_name)
    if not match:
        return old_file_name + '.rot13'
    else:
        return old_file_name[0:-6]


def read_file(file_name):
    letters = []
    file = open(file_name, 'r')

    for l in file.read():
        letters.append(l)

    file.close()
    return letters


def crypt_file(old_file, new_file):
    new_file = open(new_file, 'w')

    for letter in read_file(old_file):
        new_file.write(rot13(letter))

    new_file.close()


def usage():
    print('usage: ', sys.argv[0], ' <file_name>')
    sys.exit(1)


def check_overwrite(file_name):
    if os.path.isfile(file_name):
        erase = input(file_name + ' already exist. Do you want to erase it? (ny) ')
        if erase == 'n':
            sys.exit(1)


def main():
    args = sys.argv

    if len(args) != 2 or not os.path.isfile(args[1]):
        usage()

    file_name = sys.argv[1]
    output_file_name = get_new_file_name(file_name)
    check_overwrite(output_file_name)
    crypt_file(file_name, output_file_name)


if __name__ == '__main__':
    main()
