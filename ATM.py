# define the account balances
account_balances = {
    "MOH"  : 1000,
    "SAYED": 500,
    "AHMED": 200
}

# define the account PINs
account_pins = {
    "MOH": 1234,
    "SAYED": 5678,
    "AHMED": 9012
}

# define a function to check if an account exists
def account_exists(account_name):
    return account_name in account_balances

# define a function to check if a PIN is correct
def is_correct_pin(account_name, pin):
    return account_name in account_pins and account_pins[account_name] == pin

# define a function to withdraw money
def withdraw_money(account_name, amount):
    if account_exists(account_name):
        if account_balances[account_name] >= amount:
            account_balances[account_name] -= amount
            print(f"Withdrew {amount} from {account_name}'s account. New balance: {account_balances[account_name]}")
        else:
            print(f"Insufficient funds for {account_name}'s account.")
    else:
        print(f"Account {account_name} does not exist.")

# define a function to deposit money
def deposit_money(account_name, amount):
    if account_exists(account_name):
        account_balances[account_name] += amount
        print(f"Deposited {amount} to {account_name}'s account. New balance: {account_balances[account_name]}")
    else:
        print(f"Account {account_name} does not exist.")

# define a function to view balance
def view_balance(account_name):
    if account_exists(account_name):
        print(f"Balance for account {account_name}: {account_balances[account_name]}")
    else:
        print(f"Account {account_name} does not exist.")

# main program loop
while True:
    # get the account name and PIN from the user
    account_name = input("Enter account name: ")
    pin = int(input("Enter PIN: "))

    # check if the account and PIN are valid
    if is_correct_pin(account_name, pin):
        # show the options for the user
        print("1. Withdraw money")
        print("2. Deposit money")
        print("3. View balance")
        print("4. Exit")

        # get the user's choice
        choice = int(input("Enter choice: "))

        # perform the user's chosen action
        if choice == 1:
            amount = int(input("Enter amount to withdraw: "))
            withdraw_money(account_name, amount)
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            deposit_money(account_name, amount)
        elif choice == 3:
            view_balance(account_name)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid account name or PIN. Please try again.")