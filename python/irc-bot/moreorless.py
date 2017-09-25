from random import randint


secret_nb = 0

def moreorless(args):

    global secret_nb

    if args[0] == "start":
        secret_nb = randint(0, 999)
        return "Secret Number is defined."

    elif args[0] == "answer":
        while int(args[1]) != secret_nb:
            if int(args[1]) > secret_nb:
                return "Less !"
            elif int(args[1]) < secret_nb:
                return "More !"
        return "You win !" + str(secret_nb) + "is the Secret Number !"

    else:
        return "You must enter 'start' if you want to begin or 'answer' if you want to continue."

