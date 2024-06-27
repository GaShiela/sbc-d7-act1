import random

acc = {}

def create():
    accnum = str(random.randint(10000, 99999))
    acc[accnum] = {'balance': 1000}
    return accnum

def check(accnum):
    return acc.get(accnum, {}).get('balance', "Account not found.")

def transaction(accnum, amount):
    if accnum in acc and amount > 0:
        if amount > 0:
            acc[accnum]['balance'] += amount
            return f"Deposited {amount}. New balance: {acc[accnum]['balance']}"
        elif acc[accnum]['balance'] >= amount:
            acc[accnum]['balance'] -= amount
            return f"Withdrew {amount}. New balance: {acc[accnum]['balance']}"
        else:
            return "Insufficient funds."
    return "Invalid account or transaction amount."

def delacc(accnum):
    if accnum in acc:
        del acc[accnum]
        return "Account deleted."
    return "Account not found."

while True:
    print("\nMy Bank")
    print("CA - Create Account")
    print("CB - Check Balance")
    print(" D - Deposit")
    print(" W - Withdraw")
    print("DA - Delete Account")
    print(" E - Exit")
    choice = input("Enter your choice: ").strip().upper()
    
    if choice == 'CA':
        account_id = create()
        print(f"Account number: {account_id}")
    
    elif choice in {'CB', 'D', 'W', 'DA'}:
        accnum = input("Account number: ").strip()
        
        if choice == 'CB':
            print(f"Balance: {check(accnum)}")
        
        elif choice in {'D', 'W'}:
            amount = float(input(f"Amount to {'deposit' if choice == 'D' else 'withdraw'}: "))
            print(transaction(accnum, amount))
        
        elif choice == 'DA':
            print(delacc(accnum))
    
    elif choice == 'E':
        print("Exit.")
        break
    
    else:
        print("Invalid choice.")