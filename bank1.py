accounts = {}

def create_account():
    name = input("Enter your name: ")
    acc_no = input("Enter account number: ")
    pin = input("Set 4-digit PIN: ")

    if acc_no in accounts:
        print("Account already exists!")
    else:
        accounts[acc_no] = {
            "name": name,
            "balance": 0,
            "pin": pin,
            "transactions": []
        }
        print("Account created successfully!")

def verify_account(acc_no):
    if acc_no in accounts:
        entered_pin = input("Enter PIN: ")
        if accounts[acc_no]["pin"] == entered_pin:
            return True
        else:
            print("Wrong PIN!")
            return False
    else:
        print("Account not found!")
        return False

def deposit():
    acc_no = input("Enter account number: ")
    if verify_account(acc_no):
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount!")
            return
        accounts[acc_no]["balance"] += amount
        accounts[acc_no]["transactions"].append(f"Deposited {amount}")
        print("Deposit successful!")

def withdraw():
    acc_no = input("Enter account number: ")
    if verify_account(acc_no):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount!")
            return
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            accounts[acc_no]["transactions"].append(f"Withdrew {amount}")
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

def check_balance():
    acc_no = input("Enter account number: ")
    if verify_account(acc_no):
        print("Name:", accounts[acc_no]["name"])
        print("Balance:", accounts[acc_no]["balance"])

def show_transactions():
    acc_no = input("Enter account number: ")
    if verify_account(acc_no):
        print("\nTransaction History:")
        for t in accounts[acc_no]["transactions"]:
            print("-", t)

def show_all_accounts():
    print("\nAll Accounts:")
    for acc_no, details in accounts.items():
        print(f"Account No: {acc_no}, Name: {details['name']}, Balance: {details['balance']}")

while True:
    print("\n------ BANK MENU ------")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Show All Accounts (Admin)")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        show_transactions()
    elif choice == "6":
        show_all_accounts()
    elif choice == "7":
        print("Thank you for using our bank system!")
        break
    else:
        print("Invalid choice! Try again.")