import json
import os

def main():
    print("Hello And Welcome To RealMasterChief's Bank, The Best In The World Of Online Banking.")
    while True:
        answer=input("Do you have an account already? [Y/N]: ")
        answer=answer.upper()
        if answer not in ["N","Y"]:
            print("Input not recognized. Please try again.")
            continue
        elif answer=="N":
            account_name, account_balance,account_list=create_account()
        elif answer=="Y" and not os.path.exists('account.json'):
            print("You do not have an existing account.")
            print("Do you want to create an account, press ['C'].")
            print("Do you want to log out, press ['L'].")
            while True:
                choice=input("Choice: ")
                choice=choice.upper()
                if choice not in ["Q","C"]:
                    print("Input not recognized. Please try again.")
                    continue
                if choice=="Q":
                    
                    break
                elif choice=="C":
                    account_name,account_balance,account_list=create_account()
                    break
        elif answer=="Y":
            account_name,account_balance,account_list = login_user()  
        logged_in = True   
        print(f"Welcome {account_name} to your account.")
        print(f"Balance: {account_balance}$")
        print()
        while logged_in:
            choice=interact_with_user()
            choice = choice.upper()
            if choice == "L":
                logged_in = False
            elif choice == "U":
                print(f"Username is: {account_name}")
                back_to_main_menu()
            elif choice=="D":
                print(f"Balance: {account_balance}$")
                account_balance=deposit(account_name,account_balance,account_list)
                print(f"Updated Balance: {account_balance}$")
                back_to_main_menu()
            elif choice=="W":
                print(f"Balance: {account_balance}$")
                account_balance=withdrawal(account_name,account_balance,account_list)
                print(f"Updated Balance: {account_balance}$")
                back_to_main_menu()
            elif choice=="T":
                if account_balance==0:
                    print("You do not have the minimum balance to transfer.")
                    back_to_main_menu()
                    break
                print(f"Balance: {account_balance}$")
                account_balance=transfer(account_name,account_balance,account_list)
                print(f"Updated Balance: {account_balance}$")
                back_to_main_menu()
            elif choice=="S":
                if not os.path.exists('transactions.json'):
                    print("You do not have a transaction history.")
                    back_to_main_menu()
                    break
                choice=show_transactions_choice()
                if choice=="A":
                    view_all_transactions(account_name)
                    back_to_main_menu()
                elif choice=="S":
                    view_specific_transactions(account_list)
                    back_to_main_menu()
                


def back_to_main_menu():
    while True:
        back=input("To go back to Main Menu, press ['B']: ")
        back=back.upper()
        if back!="B":
            print("Input not recognized. Please try again.")
            continue
        break
    return back

def create_account():
    account_list=[]
    while True:
        print("It's time to create an account!")
        while True:
            account_same=False
            account_name=input("Please Enter an account name: ")
            if os.path.exists('account.json'):
                with open('account.json','r') as p:
                    account_list=json.load(p)
                    for i in account_list:
                        if i[0]==account_name:
                            print("Username taken. Please try again.")
                            account_same=True
                            break
            if account_same==True:
                        continue
            break
            
                
        account_balance=0
    
        if os.path.exists('account.json'):
            with open('account.json','r') as p:
                account_list=json.load(p)
        with open('account.json','w') as p:
            account_list.append([account_name,account_balance])
            json.dump(account_list,p)
        print("Account was created successfully.")
        break
    return account_name,account_balance,account_list
  
def login_user():
    with open("account.json", "r") as f:
        account_list = json.load(f)
    account_found = False
    while not account_found:
        account_name = input("Please enter an account name: ")
        for i in account_list:
            if i[0] == account_name:
                account_found = True
                
                account_balance = i[1]
        if not account_found:
            print("Account does not exist. Please try again.")
            continue
    return account_name, account_balance, account_list


def interact_with_user():
    print("Do you want to...")
    print("1.Show username, press ['U'].")
    print("2.Deposit, press ['D'].")
    print("3.Withdraw, press ['W'].")
    print("4,Transfer, press ['T']")
    print("5.Show transactions, press ['S'].")
    print("6.Logout, press ['L'].")
    while True:
        choice=input("Choice: ")
        choice = choice.upper()
        if choice not in ["L","U","D","W","T","S"]:
            print("Input not recognized. Please try again.")
            continue
        break
    return choice
def deposit(account_name,account_balance,account_list):
    while True:
        amount=input("How much do you want to deposit: ")
        if not amount.isdigit():
            print("Amount must be a number. Please try again.")
            continue
        amount=int(amount)
        for i in account_list:
            if i[0] == account_name:
                i[1]=int(account_balance)+amount
                account_balance=i[1]
        break
    with open('account.json','w') as p:
        json.dump(account_list,p)
    return account_balance
def withdrawal(account_name,account_balance,account_list):
    while True:
        amount=input("How much do you want to withdraw: ")
        if not amount.isdigit():
            print("Amount must be a number. Please try again.")
            continue
        amount=int(amount)
        if amount>int(account_balance):
            print("Amount can not be greater than balance. Please try again.")
            continue
        for i in account_list:
            if i[0] == account_name:
                i[1]=int(account_balance)-amount
                account_balance=i[1]
        break
    with open('account.json','w') as p:
        json.dump(account_list,p)
    return account_balance
def transfer(account_name,account_balance,account_list):
    transactions=[]
    while True:
        account_found=False
        account_name2=input("Please enter the account name you would like to transfer to: ")
        for i in account_list:
            if i[0]==account_name2:
                print("Account exists.")
                account_found=True
                break
        if account_found==False:
            print("Account does not exist, please enter a valid account name.")
            continue
        amount=input("How much would you like to transfer?: ")
        if not amount.isdigit():
            print("Amount must be a number. please try again")
            continue
        amount=int(amount)
        if amount>account_balance:
            print("Amount can not be greater than account balance. Please try again.")
            continue
        elif amount<=0:
            print("Amount can not be 0 or less. Please try again.")
            continue
        for i in account_list:
            if i[0]==account_name:
                i[1]=i[1]-amount
            if i[0]==account_name2:
                i[1]=i[1]+amount
        with open('account.json','w') as p:
            json.dump(account_list,p)
        if os.path.exists('transactions.json'):
            with open('transactions.json','r') as p:
                transactions=json.load(p)
        with open('transactions.json','w') as p:
            transactions.append([account_name,amount,account_name2])
            json.dump(transactions,p)
        break
    return account_balance-amount
def show_transactions_choice():
    print("do you want to...")
    print("1.View transactions to a specific person, press ['S'].")
    print("2.View all transactions, press ['A'].")
    while True:
        choice=input("Choice: ")
        if choice.isdigit():
            print("Input not recognized. Please try again.")
        choice=choice.upper()
        if choice not in ["S","A"]:
            print("Input not recognized. Please try again.")
        break
    return choice
def view_all_transactions(account_name):
    with open('transactions.json','r') as p:
        transactions=json.load(p)
    for i in transactions:
        if i[0]==account_name:
            print(f"Transaction was made to {i[2]} of an amount of {i[1]}$")
def view_specific_transactions(account_list):
    account_found=False
    while True:
        account_name2=input("Please enter the specific account name: ")
        for i in account_list:
            if i[0]==account_name2:
                print("Account exists.")
                account_found=True
        if account_found==False:
            print("Account does not exist. Please try again.")
            continue
        break
    with open('transactions.json','r') as p:
        transactions=json.load(p)
    for i in transactions:
        if i[2]==account_name2:
            print(f"Transaction was made to {i[2]} of an amount of {i[1]}$")
        
main()
