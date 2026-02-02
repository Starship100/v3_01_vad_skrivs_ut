
# 1a
answer = 0
for i in range(0, 11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

print("-----------------")

# 1b
answer = 0
i = 0
while i < 100:
    i += 1
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

print("-----------------")

# 2
number_list = [1, -2, 3, -2, 4, -3]
sum = 0
for number in number_list:
    sum = sum + number
print(sum)

print("-----------------")

# 3a
film = "Alien, Interstellar, Avatar, Predator"
film_list = film.split()
for token in film_list:
    film_list = film.strip()
print(film_list)