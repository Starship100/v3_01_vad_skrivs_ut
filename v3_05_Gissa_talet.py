import random

secret_nr = random.randint(1,100)
print("Välkommen till gissa talet! Gissa på ett tal mellan 1 och 100: ")
random_tal = int(input("Gissa: "))

while random_tal != secret_nr:

    if random_tal < secret_nr:
        print("Nej, det är för lågt! ")
        random_tal = int(input("Gissa: "))
    elif random_tal > secret_nr:
        print("Nej, det är för högt!")
        random_tal = int(input("Gissa: "))
else:
    #random_tal == secret_nr:
        print("Det är rätt!")