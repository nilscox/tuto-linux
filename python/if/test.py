from exos import *

def a(f, args, expected):
    if f(*args) != expected:
        print('[\033[31mKO\033[0m] ' + f.__name__ + '(' + ', '.join(map(str, args)) + ')')
    else:
        print('[\033[32mOK\033[0m] ' + f.__name__ + '(' + ', '.join(map(str, args)) + ')')

def test_isPositive():
    try: isPositive
    except NameError: return
    a(isPositive, [42], True)
    a(isPositive, [123456789], True)
    a(isPositive, [-1], False)
    a(isPositive, [-123456789], False)
    a(isPositive, [0], None)

def test_isOdd():
    try: isOdd
    except NameError: return
    a(isOdd, [2], False)
    a(isOdd, [3], True)
    a(isOdd, [0], False)
    a(isOdd, [123456789], True)
    a(isOdd, [876543210], False)
    a(isOdd, [-1], True)
    a(isOdd, [-2], False)

def test_isVowel():
    try: isVowel
    except NameError: return
    a(isVowel, ['a'], True)
    a(isVowel, ['y'], True)
    a(isVowel, ['b'], False)
    a(isVowel, ['8'], False)

def test_max():
    try: max
    except NameError: return
    a(max, [1, 2], 2)
    a(max, [2, 1], 2)

def test_max3():
    try: max3
    except NameError: return
    a(max3, [1, 2, 3], 3)
    a(max3, [1, 3, 2], 3)
    a(max3, [2, 1, 3], 3)
    a(max3, [2, 3, 1], 3)
    a(max3, [3, 1, 2], 3)
    a(max3, [3, 2, 1], 3)

def test_daysInMonth():
    try: daysInMonth
    except NameError: return
    a(daysInMonth, [1], 31)
    a(daysInMonth, [2], 28)
    a(daysInMonth, [4], 30)
    a(daysInMonth, [7], 31)
    a(daysInMonth, [8], 31)
    a(daysInMonth, [9], 30)
    a(daysInMonth, [12], 31)

for f in [
    test_isPositive,
    test_isOdd,
    test_isVowel,
    test_max,
    test_max3,
    test_daysInMonth,
]:
    print(f.__name__)
    print(len(f.__name__) * '-')
    f()
    print()
