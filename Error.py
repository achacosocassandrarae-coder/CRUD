balance = 1000000 

while True:
    print("\nCurrent Balance:", balance)

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount > balance:
            print("Insufficient funds!")

            print("\nOptions:")
            print("1. Check Balance")
            print("2. Try Again")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                print("Your balance is:", balance)

            elif choice == "2":
                continue

            elif choice == "3":
                print("Thank you!")
                break

            else:
                print("Invalid choice")

        else:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)

    except:
        print("Invalid input! Please enter a number.")
