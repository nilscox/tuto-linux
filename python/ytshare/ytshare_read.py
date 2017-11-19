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


def get_html():
    html = '<!DOCTYPE html>'
    html += '<html>'
    html += '<head>'
    html += '<title>playlist</title>'
    html += '</head>'
    html += '<body>'

    for url in read_urls():
        html += '<p>'
        html += '<iframe width="560" height="315" src="'
        html += url[:-1]
        html += '" frameborder="0" gesture="media" allowfullscreen></iframe>'
        html += '</p>'

    html += '</body>'
    html += '</html>'

    return html


def main():

    if len(sys.argv) == 1:
        for url in read_urls():
            print(url)
    else:
        print('usage:', sys.argv[0])
        sys.exit(1)


if __name__ == '__main__':
    main()
