
# 1a
answer = 0
for i in range(0, 11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

print("="*35)

# 1b
answer = 0
# for i in range(0, 101):
#     answer += i
i = 0
while i < 100:
    i += 1
    answer += i
print("Summan av talen 1 till 100 är: " + str(answer))

print("="*35)

# 2
number_list = [1, -2, 3, -2, 4, -3]
sum = 0
for number in number_list:
    sum += number
print(sum)

print("="*35)

# 3a
film = ["Alien", "Interstellar", "Avatar", "Predator"]
print(film)
film.append("Fellowship of the ring")
print(film)
film.insert(0, "The two towers")
print(film)
index = film.index("Fellowship of the ring")
print(index)
film.remove("Interstellar")
print(film)
index = film.index("Fellowship of the ring")
print(index)
print(len(film))
film.reverse()
print(film)
film.sort(reverse=True)
print(film)

print("="*75)