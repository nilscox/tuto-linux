import sys
import os


def rot13(text):
    def rot13chr(c):
        if not ("a" <= c <= "z" or "A" <= c <= "Z"):
            return c

        offset = ord("A" if c.isupper() else "a")
        n = ord(c) - offset
        n = (n + 13) % 26

        return chr(n + offset)

    result = ""

    for letter in text:
        result += rot13chr(letter)

    return result


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()


def write_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)


def get_output_filename(filename):
    if filename.endswith(".rot13"):
        return filename[:-6]
    else:
        return filename + ".rot13"


def check_overwrite(filename):
    if not os.path.isfile(filename):
        return True

    r = input(filename + " already exists. Overwrite? [yn] ")

    return r == "y" or r == "Y"


def usage():
    print("usage: " + sys.argv[0] + " <filename>")
    sys.exit(1)


def main():
    args = sys.argv[1:]

    if len(args) != 1:
        usage()

    input_filename = args[0]
    output_filename = get_output_filename(input_filename)

    if not os.path.isfile(input_filename):
        usage()

    check_overwrite(output_filename)

    input_str = read_file(input_filename)
    output_str = rot13(input_str)

    write_file(output_filename, output_str)


if __name__ == "__main__":
    main()
