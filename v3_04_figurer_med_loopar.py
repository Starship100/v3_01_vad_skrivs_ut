
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

print("-" * 30)

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3:
            s += "#"
        elif x == 4:
            s += "#"
        elif x == 5:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3:
            s += "#"
        elif x == 4:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)