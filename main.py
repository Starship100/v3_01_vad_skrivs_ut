"""""
# Skriver ut: 5,7,9,11,13,15
limit = 15
index = 5
while index <= limit:
    print(index)
    index = index + 2
    # Svar: 5,7,9,11,13,15

print("-----------------")

# Skriver ut: 1,2,3,4,""
for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
    i = i + 1
    # Svar: 0,1,2,3,4, ,6,7,8,9

print("-----------------")

# Skriver ut: 0,1,2,3,4,5
counter = 0
#for i in range(1000):
for i in range(6):
    counter += i
    print(counter)
    # Svar: 0,1,3,6,10,15

print("-----------------")
"""""
# Fattar absolut INGENTING!
x = 0
y = 1
while x < 10:
    if y % 2 == 0:  # Jämna tal delbart med 2
        x -= y     # Dra bort från x
    else:
        x += y * y  # Udda tal (y * y + x)
    y += 1
    print(x)
# Skriver ut: 1,-1,8,4,29

print("-----------------")

# Gör så den skriver ut 'time' istället
message = "its_time_to_get_coding"
print(message[4:8])
# Nailed it

print("-----------------")

# Flytta linjen ett steg åt höger
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += ","
    print(s)
# Nailed it