import json


def main():
    account_name,account_balance=create_account()
    account_name,account_balance=login_user(account_name,account_balance)
    while True:
        choice=interact_with_user()
        while True:
            if choice in ["Q","q"]:
                exit()
            elif choice in ["U","u"]:
                print(f"Username is: {account_name}")
                print()
            break
        continue



def create_account():
    global account_list
    global answer
    global account_name
    global account_balance
    account_list=[]
    print("Hello And Welcome To RealMasterChief's Bank, The Best In The World Of Online Banking.")
    while True:
        answer=input("Do you have an account already? [Y/N]")
        answer=answer.upper()
        if answer not in ["Y","N"]:
            print("Input not recognized. Please try again.")
            continue
        if answer=="Y":
            break
        print("It's time to create an account!")
        account_name=input("Please Enter an account name: ")
        account_balance=0
        with open('account.json','w') as p:
            json.dump([[account_name,account_balance]],p)
        print("Account was created successfully.")
        break
    if answer=="Y":
        account_name="nothing"
        account_balance="nothing"
    return account_name,account_balance
def login_user(account_name,account_balance):
    while True:
        if answer=="N":
            break
        elif answer=="Y":
            account_found=False
            with open('account.json','r') as p:
                account_list=json.load(p)
        while True:
            account_name=input("Please enter an account name: ")
            for i in account_list:
                if i[0]==account_name:
                    account_found=True
                    account_balance=i[1]
                    break
            if account_found==False:
                print("Account does not exist. Please try again.")
                continue
            break
        break
    return account_name, account_balance
def interact_with_user():
    print("Do you want to...")
    print("1.Show username, press [U].")
    print("2.Quit, press [Q].")
    while True:
        choice=input("Choice: ")
        if choice not in ["Q","q","U","u"]:
            print("Input not recognized. Please try again.")
            continue
        break
    return choice

main()
