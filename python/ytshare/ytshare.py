import sys
import re
from urllib.request import Request, urlopen


def save_youtube_id(youtube_id):
    p = open('playlist.txt', 'a')
    p.write(youtube_id + "\n")
    p.close()

    return '<html><body></body></html>'


def get_youtube_id(url):
    match = re.match("(https?://)?(www.)?youtube.com/watch\?v=(.*)", url)
    if match:
        return match.group(3)

    match = re.match("(https?://)?(www.)?youtu.be/(.*)", url)
    if match:
        return match.group(3)

    match = re.match("(https?://)?(www.)?youtube.com/embed/(.*)", url)
    if match:
        return match.group(3)


def usage():
    print("usage:", sys.argv[0], "<youtube-url>")
    sys.exit(1)


def main():

    if len(sys.argv) != 2:
        usage()

    youtube_id = get_youtube_id(sys.argv[1])
    req = Request('http://localhost:4269/', data=youtube_id.encode())
    urlopen(req)


if __name__ == '__main__':
    main()
