from bot import Bot
from lol import lol
from moreorless import moreorless
from hangman import hangman
from join import join
from chanmsg import chanmsg


def echo(bot, args):
    return " ".join(args)


functable = []
functable.append(echo)
functable.append(lol)
functable.append(moreorless)
functable.append(hangman)
functable.append(join)
functable.append(chanmsg)

bop = Bot(functable)
bop.connect("localhost", 6667, "bop")
bop.start()
