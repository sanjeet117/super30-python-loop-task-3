# Basic ATM simulation loop for balance check, deposit, and withdraw.
balance = 10000.00

while True:
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice from 1 to 4: ").strip()

    if choice == "1":
        print(f"Your account balance is: {balance:.2f}")
    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"The updated balance is: {balance:.2f}")
        else:
            print("Enter a valid amount")
    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"The updated balance is: {balance:.2f}")
        elif amount > balance:
            print("Insufficient balance to withdraw")
        else:
            print("Enter a valid amount")
    elif choice == "4":
        print("Thank you for using the ATM")
        break
    else:
        print("Enter a valid choice from 1 to 4")
