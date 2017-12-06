def in_dict(str):
    a = str.split('+')
    b = {}
    for i in a:
        key, value = i.split('=')
        b[key] = value

    return b