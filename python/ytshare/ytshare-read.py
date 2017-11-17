import sys
import os


def read_urls():

    urls = []

    if not os.path.isfile('playlist.txt'):
        return []

    else:
        p = open('playlist.txt', "r")
        line = p.readline()
        while line:
            urls.append(line)
            line = p.readline()

        return urls


def main():

    if len(sys.argv) == 1:
        for url in read_urls():
            print(url)
    else:
        print("usage:", sys.argv[0])
        sys.exit(1)


if __name__ == '__main__':
    main()
