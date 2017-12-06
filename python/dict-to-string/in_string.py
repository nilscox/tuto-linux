def in_string(dict):
    string = "="
    l = ""
    a = dict.items()
    for i in a:
        l += "+" + string.join(i)
    return l[1:]
