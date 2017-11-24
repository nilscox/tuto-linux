import sys
import os
import re


def rot13(letter):

    up_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    low_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', ' w', 'x', 'y', 'z']

    if letter in up_a:
        x = int(up_a.index(letter))
        if x < 13:
            new_letter = up_a[x + 13]
            return new_letter
        else:
            new_letter = up_a[x - 13]
            return new_letter
    elif letter in low_a:
        y = int(low_a.index(letter))
        if y < 13:
            new_letter = low_a[y + 13]
            return new_letter
        else:
            new_letter = low_a[y - 13]
            return new_letter
    else:
        return letter


def create_new_file(old_file):

    match = re.match("((.+)\.rot13)", old_file)
    if not match:
        new_file = old_file + '.rot13'
        file = open(new_file, 'w')
        file.close()
    else:
        new_file = old_file[0:-6]
        file = open(new_file, 'w')
        file.close()


def main():

    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        print('usage: ', sys.argv[0], ' <file_name>')
        sys.exit(1)


if __name__ == '__main__':
    main()
