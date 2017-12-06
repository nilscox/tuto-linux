def in_dict(str):
    a = str.replace('=', '+')
    list = a.split('+')
    dict = {}

    for i in list[::2]:
        j = list.index(i) + 1
        dict[i] = list[j]

    return dict
