# AUTHOR
# Dhruv

# =========================
# ATM SYSTEM (RAW PYTHON)
# =========================

filename = "atm.txt"
try :

    with open (filename , "r") as f:
        lines = f.readlines()

except FileNotFoundError :
    open (filename , "w").close()
    lines = []

accounts = {}

for line in lines:
    line = line.strip()

    if not line:
        continue

    acc_no , name , balance , pin = line.split()

    accounts[acc_no] = {
        "name": name,
        "balance": int(balance),
        "pin": pin,
        "history": []
    }

def save_accounts (filename , accounts):

    with open (filename , "w") as f:
        for acc_no , data in accounts.items():
          f.write(f"{acc_no} {data['name']} {data['balance']} {data['pin']}\n") 


def Creat_account ():

    acc_no = input("Enter your account number :").strip()

    if not acc_no.isdigit() or len(acc_no) != 10:
        print("Invalid account number!")
        return
    
    if acc_no in accounts:
        print("Account already exists!")
        return
    
    name = input("Enter your name :")

    balance = input("Enter your starting amount :")
    if not balance.isdigit():
        print("Invalid amount!")
        return   
    balance = int(balance)

    pin = input("Enter your 4-digit pin :").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("Invalid pin!")
        return
    
    accounts[acc_no] = {
        "name": name,
        "balance": balance,
        "pin": pin,
        "history": []
    }

    save_accounts (filename , accounts)

    print ("Account created successful.")

def login ():

    acc_no = input("Enter your account number :").strip()

    if acc_no not in accounts:
        print("Invalid account number!")
        return None

    for attempts in range (3):

        pin = input("Enter your 4-digit pin :").strip()
        if pin == accounts[acc_no]["pin"]:
            print("Login successfully.")
            return acc_no        
        else:
            remaining_attempts = 2 - attempts
            print(f"Total remaining attemtp(s) {remaining_attempts}")

    print("Too many wrong attempts!")
    return None  

def Exit ():
    # you can make this without using def function.
    print("Thank you for using ATM.")

def Deposit (acc_no):   

    amount = input("Enter an amount for deposit :").strip()

    if not amount.isdigit():
        print(f"Invalid amount :{amount}")
        return

    amount = int(amount)

    if amount <= 0:
        print("Amount must be greater than zero!")
        return
    
    accounts[acc_no]["balance"] += amount
    
    accounts[acc_no]["history"].append(f"+{amount} deposited.")

    save_accounts (filename , accounts)

    print("Your money deposited successfully.")

def Withdraw (acc_no):

    amount = input("Enter an amount for withdraw").strip()

    if not amount.isdigit():
        print(f"Invalid amount {amount}")
        return

    amount = int(amount)

    if amount <= 0:
        print("Amount must be greater than zero!")
        return

    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance.")
        return
    
    accounts[acc_no]["balance"] -= amount

    accounts[acc_no]["history"].append(f"-{amount} withdrawn")

    save_accounts (filename , accounts)

    print("Your money withdrawn successfully.")

def Transfer (acc_no):

    reciver_account_no = input("Enter reciver account number :")

    if not reciver_account_no.isdigit() or len(reciver_account_no) != 10:
        print("Accoun number must bee numbers!")
        return
    
    if reciver_account_no not in accounts:
        print("Reciver account does not exsist!")
        return
    
    if reciver_account_no == acc_no:
        print("You can't transter to your self!")
        return

    amount = input("Enter an amount to transfer..")

    if not amount.isdigit():
        print("Invalid amount!")
        return
    amount = int(amount)

    if amount <= 0:
        print("Amount must be greater than zero!")
        return
    
    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance")
        return
    
    accounts[acc_no]["balance"] -= amount

    accounts[reciver_account_no]["balance"] += amount

    accounts[acc_no]["history"].append (f"-{amount} sent to {reciver_account_no}")

    accounts[reciver_account_no]["history"].append (f"+{amount} received from {acc_no}")

    save_accounts(filename, accounts)

    print("Transfer successful.")

def View_transaction_history (acc_no):

    history = accounts[acc_no]["history"] 

    if not history:
        print("No transaction yet!")
        return
    
    print("\n--- Last Transactions ---")

    for record in history[-5:][::-1]:
        print(record)

def Check_balance (acc_no):

    balance = accounts[acc_no]["balance"]

    if balance == 0:
        print(f"You have {0} blance")
        return

    else:
        print(f"You have {balance} balance")

def Logut (acc_no):

    print("Logged out.")

def Season_menu (acc_no):

    while True:

        print("\n--- ATM SESSION MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Logout")

        userchoice = input("Choce any one option.")

        if userchoice == "1":
            Deposit(acc_no)

        elif userchoice == "2":
            Withdraw(acc_no)

        elif userchoice == "3":
            Transfer(acc_no)

        elif userchoice == "4":
            Check_balance(acc_no)

        elif userchoice == "5":
            View_transaction_history(acc_no)

        elif userchoice == "6":
            Logut(acc_no)
            break

        else:
            print("Invalid option.")


def main_menu ():

    while True:

        print("\n--- MAIN MENU ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        userchoice = input("Choce any one option.")

        if userchoice == "1":
            Creat_account()
        
        elif userchoice == "2":
            user = login()

            if user:
                Season_menu(user)

        elif userchoice == "3":
            Exit()
            break

        else:
            print("Invalid option!")

# PROGRAM START FROM HERE

main_menu()