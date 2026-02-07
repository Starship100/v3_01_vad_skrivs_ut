
print("*** Todo List ***")

todo_list = []

while True:
    print("1. Se innehållet i din lista")
    print("2. Lägg till nya punkter till din lista")

    choice = input("Välj ett alternativ: ")

    if choice == "1":
        if len(todo_list) == 0:
            print("Listan är tom")
        else:
            for item in todo_list:
                print(item)

    elif choice == "2":
        todo_list = input("Lägg till: ")




# input = input("Lägg till saker i din Todo-list: ")
# todo_list = input.split(",")

#print(todo_list)