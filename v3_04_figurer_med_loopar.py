for y in range(1, 10):
    s = ""
    for x in range(1, 20):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)