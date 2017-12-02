def fibo(n):
    tab = [0, 1]
    x = 1

    while n > len(tab):
        tab.append(tab[x - 1] + tab[x])
        x += 1

    return tab[:n]
