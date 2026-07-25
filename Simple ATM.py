# Simple ATM 
balance = 1000
correct_pin = "1234"

pin = input("Enter your PIN: ")

if pin == correct_pin:
    print("Login Successful")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")

    def check_balance(balance):
        print("Balance :", balance)
        return balance

    def deposit(balance):
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposit Successful")
        print("New Balance:", balance)
        return balance


    def withdraw(balance):
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")

        return balance


    choice = input("Enter your choice: ")

    if choice == "1":
        balance = check_balance(balance)

    elif choice == "2":
        balance = deposit(balance)

    elif choice == "3":
        balance = withdraw(balance)

    else:
        print("Invalid Choice")

else:
    print("Incorrect PIN")

