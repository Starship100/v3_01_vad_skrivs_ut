
print("Välkommen till Kvittouträknaren! ")
print("Avsluta genom att skriva 'quit' eller 'avsluta'.")

antal_personer = int(input("Hur många personer är ni? "))
user_input = input("Skriv in ett belopp: ")  # Lagrar användarens inmatade belopp. Används igen i while loop nedan

summa_tal = 0

# Loopa användares svar tills avslut
# while user_input != "q" and user_input != "quit" and user_input != "avsluta":
while user_input not in ["q", "quit", "avsluta"]:
    summa_tal += int(user_input)
    user_input = input("Skriv in ett belopp: ")

# Användaren har avslutat "Skriv in ett belopp: "
# Hur mycket dricks vill användaren lägga?
dricks_input = input("Hur många procent dricks vill ni lägga? ")

dricks_procent = 0

if dricks_input == "":  # Om användare inte anger ngt värde = automatiskt 10% dricks
    #dricks_input = summa_tal * 0.10
    dricks_procent = 10
else:
    dricks_procent = float(dricks_input) # Lägg inmatad % i variabeln 'dricks_procent'

dricks_belopp = summa_tal * (dricks_procent / 100)  #
total_med_dricks = summa_tal + dricks_belopp  # Ny variabel lägger ihop summan av tal och dricks

summa_per_person = total_med_dricks / antal_personer

print("Det blir " + str(total_med_dricks) + "kr totalt, alltså " + str(summa_per_person) + "kr per person. Välkommen åter!")