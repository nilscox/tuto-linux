import sys


def save_url(url):
    p = open('playlist.txt', 'a')
    p.write(url + "\n")
    p.close()


def main():

    tab = sys.argv
    url = tab[1]

    if len(tab) == 2:
        save_url(url)
    else:
        print("usage:", tab[0], "<youtube-url>")
        sys.exit(1)


if __name__ == '__main__':
    main()
