
print("Välkommen till Kvittouträknaren! ")
print("Avsluta genom att skriva 'quit' eller 'avsluta'.")

summa_tal = 0
antal_personer = float(input("Hur många personer är ni? "))
user_input = input("Skriv in ett belopp: ")

#while user_input != "q" and user_input != "quit" and user_input != "avsluta":
while user_input not in ["q", "quit", "avsluta"]:
    summa_tal += int(user_input)
    user_input = input("Skriv in ett belopp: ")

summa_per_person = summa_tal / antal_personer
print("Det blir " + str(summa_tal) + "kr totalt, alltså " + str(summa_per_person) + "kr per person. Välkommen åter!")