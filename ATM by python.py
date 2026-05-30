# Accounts details (card.no , pin , balance)
data = {
    1204: {"pin": 4444, "balance": 12000},
    1205: {"pin": 5555, "balance": 8000},
    1206: {"pin": 6666, "balance": 15000}
}
# input form the user (card.no & pin)
cn = int(input("Enter the card number: "))
pin = int(input("Enter the pin: "))
# if statement for verifing the card.no
if cn in data:
    # if statement for verifing the pin
    if pin == data[cn]["pin"]:
        # while as a looping statement for the choices
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            # choice 1 (balance)
            if choice == 1:
                print("Current Balance:", data[cn]["balance"])
            # choice 2 (deposit)
            elif choice == 2:
                amount = float(input("Enter amount to deposit: "))
                data[cn]["balance"] += amount
                print("Amount Deposited Successfully!")
                print("Updated Balance:", data[cn]["balance"])
            # choice 3 (withdraw)
            elif choice == 3:
                amount = float(input("Enter amount to withdraw: "))
                # checks sufficient balance & subtracts withdrawal amount
                if amount <= data[cn]["balance"]:
                    data[cn]["balance"] -= amount
                    print("Withdrawal Successful!")
                    print("Remaining Balance:", data[cn]["balance"])
                else:
                    print("Insufficient Balance!")
            # choice 4 (exit)
            elif choice == 4:
                print("Thanks using the ATM.")
                break
            # error message for invalid input.
            else:
                print("Invalid Choice!")
    # error message for invalid pin.
    else:
        print("Invalid PIN!")
# error message for invalid card.no .
else:
    print("The Card Number doesn't exist.")
