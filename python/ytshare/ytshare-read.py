import sys


def read_urls():

    url =[]
    p = open('playlist.txt', "r")
    line = p.readline()
    while line:
        url.append(line)
        line = p.readline()

    return url


def main():

    if len(sys.argv) == 1:
        read_urls()
        print(read_urls())
    else:
        print("usage:", sys.argv[0])
        sys.exit(1)


if __name__ == '__main__':
    main()