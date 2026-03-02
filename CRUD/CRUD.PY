users = []
next_user = 1

while True:
    choice = input("add | update | delete | show | exit : ")

    if choice == "add":
        add = input("Add new user: ")
        users.append(add)
        print(users)

    elif choice == "update":
        update = input("Which user do you want to update? ")
        if update in users:
            index = users.index(update)
            new_value = input("Enter the new user name: ")
            users[index] = new_value
            print(users)
        else:
            print("===== User not found. =====")

    elif choice == "delete":
        remove = input("Select and delete a user: ")
        if remove in users:
            users.remove(remove)
            print(users)
        else:
            print("===== User not found. =====")

    elif choice == "show":
        if not users:
            print("===== No users found. =====")
        else:
            print("----- User List -----", users)

    elif choice == "exit":
        print(">>>>>>> Exit <<<<<<<")
        break   

    else:
        print("Invalid option. Try again.")