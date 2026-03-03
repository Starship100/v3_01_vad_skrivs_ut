#a
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)
#b
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

print("-" * 30)
#c
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or x == 4 or x == 5:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)
#d
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or y == 3:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)
#e
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 5 or x == 7 - y:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)
#f
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y or x == 7 - y:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)
#g
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1 or x == 3 or x == 5 or x == 7:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)
#h
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y == 1 or y == 6 or x == 1 or x == 8:
            s += "."
        elif y == 2 or y == 5 or x == 2 or x == 7:
            s += "#"
        else:
            s += "."
    print(s)

print("-"*30)
#i
# Använder modulo(%) = istället för att använda if x ==2 or x == 5...
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (x - y) % 3 == 0:    # (x - y) för att mönstret ska backa ett steg
            s += "."            # så att nästa rad börjar med det tecken som kom efter i förra raden
        elif (x - y) % 3 == 1:
            s += "#"
        else:
            s += "0"
    print(s)

print("-"*30)
#j
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y < 4:
            # Stolpar var tredje position
            if (x + 1) % 3 == 1:
                s += "#"
            else:
                s += "."
            # Rad med punkter
        elif  y == 4:
            s += "."
        else:
            # Schackmönster växlar beroende på (x - y)
            if (x + y) % 2 == 0:
                s += "."
            else:
                s += "#"
    print(s)