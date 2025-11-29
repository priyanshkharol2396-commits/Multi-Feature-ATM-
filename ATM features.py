import pywhatkit
import datetime

# Simple Data Store
accounts = []
account_statements = {}

# Helper functions
def print_name(name):
    print(f"Welcome {name}!")

double = lambda x: x * 2  # Example lambda usage

# Create Account
def create_account():
    name = input("Enter your name: ")
    pin = input("Set your 4-digit PIN: ")
    balance = int(input("Initial Deposit: "))
    phone = input("Enter WhatsApp number (with country code): ")
    account = (name, pin, balance, phone)
    accounts.append(account)
    account_statements[name] = []
    print_name(name)
    print("Account created successfully!")

# Find Account
def find_account(name):
    for acc in accounts:
        if acc[0] == name:
            return acc
    return None

# Deposit Money
def deposit():
    name = input("Account Name: ")
    acc = find_account(name)
    if acc:
        amount = int(input("Deposit Amount: "))
        idx = accounts.index(acc)
        acc_list = list(acc)
        acc_list[2] += amount
        accounts[idx] = tuple(acc_list)
        account_statements[name].append(f"+{amount} deposit on {datetime.datetime.now()}")
        print("Deposit successful! Current Balance:", acc_list[2])
    else:
        print("Account not found!")

# Withdraw Money
def withdraw():
    name = input("Account Name: ")
    acc = find_account(name)
    if acc:
        pin = input("Enter PIN: ")
        if pin == acc[1]:
            amount = int(input("Withdraw Amount: "))
            if amount <= acc[2]:
                idx = accounts.index(acc)
                acc_list = list(acc)
                acc_list[2] -= amount
                accounts[idx] = tuple(acc_list)
                account_statements[name].append(f"-{amount} withdrawal on {datetime.datetime.now()}")
                print("Withdrawal successful! Remaining Balance:", acc_list[2])
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect PIN")
    else:
        print("Account not found!")

# Send WhatsApp Statement
def send_statement():
    name = input("Account Name for Statement: ")
    acc = find_account(name)
    if acc:
        statement = "\n".join(account_statements[name])
        pywhatkit.sendwhatmsg_instantly(acc[3], f"Account Statement for {name}:\n{statement}")
        print("Statement sent to WhatsApp!")
    else:
        print("Account not found!")

# Advanced Features
def features():
    # Sorting accounts by balance
    sorted_accounts = sorted(accounts, key=lambda x: x[2], reverse=True)
    print("Accounts Sorted by Balance (High to Low):")
    for acc in sorted_accounts:
        print(acc[0], acc[2])

    # List comprehension: Get all balances
    balances = [acc[2] for acc in accounts]
    print("Balances:", balances)

    # String ops: Find accounts with 'a' in name
    print("Accounts with 'a' in name:", [acc[0] for acc in accounts if 'a' in acc[0].lower()])

    # Sets: Unique balances
    print("Unique balances:", set(balances))

    # Dictionaries: name to balance
    account_dict = {acc[0]: acc[2] for acc in accounts}
    print("Dictionary of accounts and balances:", account_dict)

    # Tuples: Access items
    if accounts:
        print("First account (as tuple):", accounts[0])
        print("Accessing items in tuple:", accounts[0][0], accounts[0][2])

    # Reverse account list
    print("Accounts reversed:", [acc[0] for acc in accounts[::-1]])

    # File Handling: Save statements
    with open('statements.txt', 'w') as f:
        for name, stmt in account_statements.items():
            f.write(f"{name}: " + "; ".join(stmt) + '\n')
    print("Statements saved to file.")

# Main Menu
def main():
    while True:
        print("\nATM Project Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Send WhatsApp Statement")
        print("5. View Features")
        print("6. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            send_statement()
        elif choice == '5':
            features()
        elif choice == '6':
            print("Exiting ATM System.")
            break
        else:
            print("Invalid Choice. Try again.")

main()
