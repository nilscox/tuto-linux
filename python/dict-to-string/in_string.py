def in_string(dict):
    tuples = [(x, dict[x]) for x in dict.keys()]
    str = ""

    for i in range(len(tuples)):
            str += tuples[i][0] + "=" + tuples[i][1] + "+"

    return str[:-1]
