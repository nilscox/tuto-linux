from bot import Bot
from lol import lol
from moreorless import moreorless
from hangman import hangman

def echo(args):
    return args


functable = []
functable.append(echo)
functable.append(lol)
functable.append(moreorless)
functable.append(hangman)

bop = Bot(functable)
bop.connect("localhost", 6667, "bop")
bop.start()
