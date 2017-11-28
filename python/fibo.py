def fibo(n):
    tab = [0, 1]
    x = 1
    y = tab.index(x)

    while n > len(tab):
        tab.append(tab[x - 1] + tab[x])
        x = x + (tab[y] + tab[y - 1])

    return tab[:n]
