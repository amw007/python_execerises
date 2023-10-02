class atm:       
    def __init__(self):
        self.total=0

    def new_acc(self,cash):
        self.total=self.total+cash
        print(self.total," rupees is deposited in the new account.")

    def withdraw(self,cash):
        if cash<self.total:
            self.total=self.total-cash
            print("Processing request for the withdrawl of ",cash," rupees.")
            print("Withdrawl success and cash after withdrawl is ",self.total)
            print("_______________________")
        else:
            print("Insufficient balance.")
            print("_______________________")

    def deposit(self,cash):
        self.total+=cash
        print("New Balance is ",self.total)
        print("_______________________")
        
    def check_balance(self):
        print("Balance is ",self.total)
        print("_______________________")


k=int(input("enter the total number of atm's available..."))
lst=[]
for i in range(k):
    lst.append("obj_{}".format(i+1))


for i in range(k):
    lst[i]=atm()
a=0
while(a!=2):
    print("1. Select atm and continue operation...\n2. Exit ATM")
    h=int(input("Enter operation..."))
    if h==1:
        s=int(input("enter the atm from which operation need to be performed..."))
        l=0
        while(l!=4):    
            print("__________ATM{}_______".format(s))
            print()
            print("0. New account\n1. Withdrawl\n2. Deposit\n3. Check Balance\n4. Change ATM")  
            i=int(input("Enter the function required...."))
            if i==0:
                x=int(input("enter the initial deposit amount..."))
                lst[s-1].new_acc(x)
            elif i==1:
                x=int(input("enter the amount need to be withdrawn..."))
                lst[s-1].withdraw(x)       
            elif i==2:
                x=int(input("enter the amount need to be deposited..."))
                lst[s-1].deposit(x)
            elif i==3:
                lst[s-1].check_balance()
            elif i==4:
                l=4
                print("________EXITING_ATM{}______".format(s))
            else:
                print("enter either 1,2,3 or 4.")    
    elif h==2:
        a=2
        print("________EXITING_ATM______")
    else:
        print("either enter 1 or 2.")


