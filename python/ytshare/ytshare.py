#!/usr/bin/python3

import sys
import re


def embed_url(url):
    url.replace("watch?v=", "embed/")
    return str(url.replace("watch?v=", "embed/"))


def save_url(url):
    p = open('playlist.txt', 'a')
    p.write(embed_url(url) + "\n")
    p.close()


def is_youtube_url(url):
    regex = re.compile("(https?://)?(www.)?youtube.com/watch\?v=.*")
    return regex.match(url)


def main():

    tab = sys.argv

    if len(tab) == 2 and is_youtube_url(tab[1]):
        save_url(tab[1])
    else:
        print("usage:", tab[0], "<youtube-url>")
        sys.exit(1)


if __name__ == '__main__':
    main()
