def dich(list, elem):
    if len(list) == 0:
        return None

    if elem > list[-1]:
        return None

    if len(list) == 1:
        return 0

    x = 0
    y = len(list) - 1
    z = (x + y)//2
    while list[z] != elem:
        if list[x] == elem:
            return x
        elif list[z] > elem:
            z //= 2
        elif list[z] < elem:
            x += 1

    return z


def verif(list, elem):
    actual = dich(list, elem)
    expected = None
    try:
        expected = list.index(elem)
    except ValueError:
        pass

    if actual == expected:
        print('[\033[32mOK\033[0m] ')
    else:
        print('[\033[31mKO\033[0m] ')


if __name__ == '__main__':
    verif([], 0)
    verif([0], 0)
    verif([0, 1], 0)
    verif([0, 1], 1)
    verif([0, 1], 2)
    verif([0, 1, 2], 0)
    verif([0, 1, 2], 1)
    verif([0, 1, 2], 2)
    verif([0, 1, 2], 3)
    verif([0, 1, 2, 3, 4, 5, 6, 7, 8], 0)
    verif([0, 1, 2, 3, 4, 5, 6, 7, 8], 1)
    verif([0, 1, 2, 3, 4, 5, 6, 7, 8], 4)
    verif([0, 1, 2, 3, 4, 5, 6, 7, 8], 6)
    verif([0, 1, 2, 3, 4, 5, 6, 7, 8], 7)
    verif([0, 1, 2, 3, 4, 5, 6, 7, 8], 8)
    verif([0, 1, 2, 3, 4, 5, 6, 7, 8], 9)
    verif([4, 31, 40, 86], 48)

