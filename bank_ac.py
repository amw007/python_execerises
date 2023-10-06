class Atm:
    def __init__(self):
        self.username = ["Amal","Anand","Abi"]
        self.password = ["am","an","ab"]
        self.balance = [1000,1234,45678] 
        self.k = (len(self.username)+1)
        self.name=""

    def new_acc(self,uname, passw, balnce):
        self.username.append(uname)
        self.password.append(passw)
        self.balance.append(balnce)
        self.k += 1

    def withdraw(self, amount):
        position = self.username.index(self.name)
        self.balance[position] -= amount
        print(f"Withdrawn {amount} and balance after withdrawl is {self.balance[position]}")

    def deposit(self, amount):
        position = self.username.index(self.name)
        self.balance[position] += amount
        print(f"Deposited {amount} and balance after deposit is {self.balance[position]}")

    def balance_acc(self):
        position = self.username.index(self.name)
        print(f"Balance available in the account is {self.balance[position]}")


atm = Atm()
print("Welcome to the atm...")
while True:
    selection = int(input("1. New User\n2. Login\n3. Exit\nEnter your choice..."))

    if selection == 1:
        new_username = input("enter the username...")
        new_password = input("enter the passworrd...")
        new_balance = int(input("enter the initial deposit..."))
        atm.new_acc(new_username, new_password, new_balance)
        continue

    elif selection==2:
        username = input("enter the username...")

        while username not in atm.username:
            username = input("enter the username...")
        for idx,acc in enumerate(atm.username):
            if username == acc:
                user_index = idx
                break
        password = input("enter the password...")
        atm.name = username
        while password != atm.password[user_index]:
            password = input("enter the correct password...")
        print(f"{atm.username[user_index]} successfully logged into the account.")
        while True:
            option = int(input("1. Withdraw\n2. Deposit\n3. Check Balance\n4. Log Out\nEnter your choice..."))

            if option == 1:
                amount = float(input("enter the amount need to be withdrawn"))
                atm.withdraw(amount)
                continue

            elif option == 2:
                amount = float(input("enter the amount need to be deposited"))
                atm.deposit(amount)
                continue

            elif option == 3:
                atm.balance_acc()
                continue

            elif option == 4:
                print("Log Out")
                break

            else:
                print("Enter a valid option.")

        continue   

    elif selection == 3:
        print("Exiting")
        break

    else:
        print("Enter valid option.")
        continue

