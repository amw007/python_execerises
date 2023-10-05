class Atm:       
    def __init__(self):
        pass

    def withdraw(self,acc,amount):
        if amount < acc.balance:
            acc.balance = acc.balance - amount
            print(f"Processing request for the withdrawl of {amount} rupees.")#
            print(f"Withdrawl success and cash after withdrawl is {acc.balance}")
            print("_______________________")
        else:
            print("Insufficient balance.")
            print("_______________________")
        return acc

    def deposit(self,acc,amount):
        acc.balance += amount
        print(f"New Balance is {acc.balance}")
        print("_______________________")
        return acc
        
    def check_balance(self,acc):
        print(f"Balance is {acc.balance}")
        print("_______________________")

class Account:
    def __init__(self,name,balance, password):
        self.name = name
        self.balance = balance
        self.password = password

username = ["amal" , "ameen" , "abu"]
password = ["am" , "ae" , "ab"]
balance = [100000 , 20331 , 34222]

acc_list = [Account(username[i], balance[i], password[i]) for i in range(len(username))]
atm = Atm()

print("Welcome to the ATM")
while True:
    option = int(input("enter the option \n1. Login\n2. Exit\n"))
    if option == 1:
        uname = input("Enter the username...")
        while uname not in username:
            uname = input("Enter the username...")
        for idx, acc in enumerate(acc_list):
            if acc.name == uname:
                userAcc = acc
                userAccIdx = idx
        passw = input("enter the password...")
        while userAcc.password != passw:
            passw = input("enter the password...")
        while True:
            selection = int(input("enter operation\n1.Withdraw\n2.Deposit\n3.Check Balance\n4.Log Out"))
            if selection == 1:
                amnt = float(input("Enter the amount need to be withdrawn..."))
                acc_list[userAccIdx] == atm.withdraw(userAcc,amnt)
                continue
            elif selection == 2:
                amnt = float(input("enter the amount need to be deposited..."))
                acc_list[userAccIdx] == atm.deposit(userAcc,amnt)
                continue
            elif selection == 3:
                atm.check_balance(userAcc)
            elif selection == 4:
                print("Logging Out")
                break
            else:
                print("Enter valid option.")
                continue
        
    elif option == 2:
        print("Exiting atm application")
        break
    else:
        print("enter a valid option.")
        continue
