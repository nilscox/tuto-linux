from random import randint


def moreorless(args):
    secret_nb = randint(0, 999999)
    n = int(input("So, what is the Secret Number ?"))

    while n != secret_nb:
         if n > secret_nb:
            return "Less !"
         elif n < secret_nb:
             return "More !"
    return "You win !" and secret_nb and "is the Secret Number !"


