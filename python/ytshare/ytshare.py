import sys
import re


def save_youtube_id(youtube_id):
    p = open('playlist.txt', 'a')
    p.write(youtube_id + "\n")
    p.close()


def get_youtube_id(url):
    match = re.match("(https?://)?(www.)?youtube.com/watch\?v=(.*)", url)
    if match:
        return match.group(3)

    match = re.match("(https?://)?(www.)?youtube.be/(.*)", url)
    if match:
        return match.group(3)

    match = re.match("(https?://)?(www)?youtube.com/embed/(.*)", url)
    if match:
        return match.group(3)


def usage():
    print("usage:", sys.argv[0], "<youtube-url>")
    sys.exit(1)


def main():

    if len(sys.argv) != 2:
        usage()

    youtube_id = get_youtube_id(sys.argv[1])
    save_youtube_id(youtube_id)


if __name__ == '__main__':
    main()
