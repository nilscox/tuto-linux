from bot import Bot
from lol import lol
from moreorless import moreorless
from hangman import Hangman

def echo(args):
    return args


functable = []
functable.append(echo)
functable.append(lol)
functable.append(moreorless)
#functable.append(hangman)

bop = Bot([Hangman])
bop.connect("192.168.1.82", 6667, "bop")
bop.start()
