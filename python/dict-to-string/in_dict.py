def in_dict(str):
    a = str.split('+')
    b = {}
    for i in a:
        c = i.split('=')
        b[c[0]] = c[1]

    return b
