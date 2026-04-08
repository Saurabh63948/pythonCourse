def atm_machine():
    pin = 1234
    balance = 5000
    pin_verified = False

    # PIN verification
    for i in range(3):
        user_pin = int(input("Enter your PIN: "))
        if user_pin == pin:
            print("PIN verified successfully")
            pin_verified = True
            break
        else:
            print("Incorrect PIN")

    if not pin_verified:
        print("Account locked ")
        return

    def check_balance():
        print(f"Your balance is: {balance}")

    def deposit_money():
        nonlocal balance  
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Updated balance: {balance}")
        else:
            print("Invalid amount")

    def withdraw_money():
        nonlocal balance   
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance ")
        elif amount <= 0:
            print("Invalid amount")
        else:
            balance -= amount
            print(f"Remaining balance: {balance}")

    # Menu loop
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            print("Thank you! Final balance:", balance)
            break
        else:
            print("Invalid choice")


atm_machine()