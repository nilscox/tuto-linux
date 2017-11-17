import sys


tab = sys.argv
url = sys.argv[1]


def save_url(url):
    p = open('playlist.txt', 'a')
    p.write(url + "\n")
    p.close()


if len(tab) == 2:
    save_url(url)
else:
    print("usage:", tab[0], "<youtube-url>")


