balance = 1000.0
pin = "1234"
transactions = []

#Check Balance Funtion
def check_balance():
    print(f"Your current balance is {balance} PKR")

#deposit money function
def deposit():
    global balance
    amount = float(input("How much amount you want to deposit ?"))
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited {amount} PKR")
        print(f" {amount} PKR deposited successfully.")
    else:
        print("Invalid Amount!")

#withdraw money function
def withdraw():
    global balance
    amount = float(input("Enter the amount :"))
    if amount > 0 and amount <= balance:
        balance -= amount
        transactions.append(f"Withdraw {amount} PKR.")
        print(f"{amount}PKR has been withdrawn successfully. ")
    elif amount > balance:
        print("You don't have sufficient balance. ")
    else:
        print("Invalid amount.")

#transaction history function
def history():
    if transactions:
        print("     Transaction History     ")
        for t in transactions:
            print("-",t)
    else:
        print("No transactions yet.")

#main function
print("Welcome to the ATM.")
#verification
attempts = 3
while attempts > 0:
    entered_pin = input("ENter your 4 digit pin. ")
    if entered_pin == pin:
        break
    else:
        attempts -= 1
        print(f"Incorrect pin {attempts} attempts left.")
if attempts == 0:
    print("Your card is blocked due to many failed attempts.")
else:
#Menu
    while True:
        print("     Main Menu    ")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Chose an option from 1-5 :")

        if choice == "1":
             check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            history()
        elif choice == "5":
            print("Thank you for using this ATM")
            break
        else:
            print("Invalid Option. Please try again.")
