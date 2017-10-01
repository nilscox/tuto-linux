from random import randint


secret_nb = 0


def start(args):

    global secret_nb

    secret_nb = randint(0, 999)
    return "Secret Number is defined."


def answer(args):

    global secret_nb

    if int(args[1]) > secret_nb:
        return "Less !"
    elif int(args[1]) < secret_nb:
        return "More !"
    else:
        return "You win ! " + str(secret_nb) + " is the Secret Number !"


def moreorless(bot, args):

    if args[0] == "start":
        return start(args)
    elif args[0] == "answer":
        return answer(args)
    else:
        return "You must enter 'start' if you want to begin or 'answer' if you want to continue."
