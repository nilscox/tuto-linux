import sys


def file():
    p = open('playlist.txt', 'a')
    p.write(sys.argv[1] + "\n")
    p.close()


tab = sys.argv

if len(tab) == 2:
    file()
else:
    print("usage: ytshare.py <youtube-url>")


