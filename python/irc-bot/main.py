from bot import Bot
from lol import lol
from moreorless import moreorless

def echo(args):
    return args


functable = []
functable.append(echo)
functable.append(lol)
functable.append(moreorless)

bop = Bot(functable)
bop.connect("192.168.1.82", 6667, "bop")
bop.start()
