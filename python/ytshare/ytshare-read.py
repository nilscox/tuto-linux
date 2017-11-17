import sys


p = open('playlist.txt', "r")
urls_list = p.read()

if len(sys.argv) == 1:
    p.read()
    print(urls_list)
    p.close()
else:
    print("usage:", sys.argv[0])
    sys.exit(1)