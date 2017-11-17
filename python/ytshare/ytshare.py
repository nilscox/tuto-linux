import sys

p = open('playlist.txt', 'a')
tab = sys.argv


if len(tab) == 2:
    p.write(sys.argv[1] + "\n")
elif len(tab) == 1:
    print("You must paste one youtube link.")
else:
    print("You can only paste one link at a time.")

p.close()