import sys

p = open('playlist.txt', 'a')

p.write(sys.argv[1] + "\n")

p.close()