#bank management system
import datetime
class Bank:
    def __init__(self,name,total_balance):
        self.name = name
        self.total_balance = total_balance
        self.user_list = {} #{account_no : user_account_object}
        self.total_loan = 0
        self.is_bankrupt = False
        self.is_loan_active = True
class User:
    def __init__(self,name,email,address,account_type,bank):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_no = len(bank.user_list) + 1
        self.transaction_history = {} #{date_time : (diposit,500)}
        self.take_loan_limit = 0
    def deposit(self,amount):
        self.balance += amount
        dt = datetime.datetime.now()
        tup = ('deposit',amount)
        self.transaction_history[dt] = tup
        print(f"\tdeposit {amount} successfully")
    def withdraw(self,amount,bank):
        if bank.is_bankrupt == False: 
            if amount <= self.balance:
                self.balance -= amount
                print(f"\twithdraw {amount} successfully")
                dt = datetime.datetime.now()
                tup = ('withdraw',amount)
                self.transaction_history[dt] = tup
            else:
                    print("\t withdraw amount excedded")
        else:
            print("\sorry bank is bankrupt")
    def check_balance(self):
        print(f"\tbalance is :{self.balance}")
    #loan nile bank er balance kome jabe
    def take_loan(self,bank,amount):
    
        if bank.is_loan_active == True:
            if amount <= bank.total_balance:
                if self.take_loan_limit < 2:
                    bank.total_loan += amount
                    bank.total_balance -= amount
                    self.balance += amount
                    self.take_loan_limit += 1
                    dt = datetime.datetime.now()
                    tup = ('loan',amount)
                    self.transaction_history[dt] = tup
                    print(f"\t {amount} tk loan successfully")
                else:
                    print("\tloan take time over")
            else:
                print("\t sorry bank has not enough money")
        else:
            print("\tsorry loan service is not available")
        

    def transfer_balance(self,account_no,amount,bank):
        if account_no in bank.user_list.keys():
            if amount <= self.balance:
                self.balance -= amount
                bank.user_list[account_no].balance += amount
                dt = datetime.datetime.now()
                tup = ('balance_transfer',amount)
                self.transaction_history[dt] = tup
                print(f"\t {amount} transfered successfully")
            else:
                print("\tyou do not have enough money to transfer")
        else:
            print("\t account does not exist")
    def delete_user_account(self,account_no,bank):
        if account_no in bank.user_list.keys():
            del bank.user_list[account_no]
            print("\t account deleted successfully")
        else:
            print("\tuser not found")
    def see_all_user(self,bank):
        for user in bank.user_list.values():
            print(f"\taccount_number : {user.account_no}, name : {user.name} , email : {user.email} , address  : {user.address} , account_type : {user.account_type} ")
    
    def total_balance(self,bank):
        print(f"\tbank er total balance : {bank.total_balance}")
    def total_loan(self,bank):
        print(f"\ttotal loan : {bank.total_loan}")
    def on_loan(self,bank):
        bank.is_loan_active = True
        print("\tloan service on successfully")
    def off_loan(self,bank):
        bank.is_loan_active = False
        print("\t loan service off successfully")
    

#replica system
#bank started with 1000000000
islami_bank = Bank("islami bank bangladesh limited" , 1000000000)
current_user = None
while True:    
    print("\t=====welcome to islami bank limited pabna=========")
    if current_user == None:
        option = input("\tyou are not a user please login or register or exit: (L/R/E)")
        if option == 'R':
            name = input("\t enter your name : ")
            email = input("\t please enter your email : ")
            address = input("\t enter your address : ")
            account_type = input("\t Enter account type : ")
            if account_type == 'savings' or account_type == 'current':
                user = User(name,email,address,account_type,islami_bank)
                islami_bank.user_list[user.account_no] = user
                current_user = user
            else:
                print("\t account type is not  valid")
        elif option == 'L':
            account_no = int(input("\t Enter your account number : "))
            match = False
            for user in islami_bank.user_list.values():
                if user.account_no == account_no:
                    match = True
                    # print(user.account_no,account_no)
                    # print(type(user.account_no),type(account_no))

                    current_user = user
                    print(f"logged into {current_user.name}")
            if match == False:
                print("\tNo account found")
        elif option == 'E':
            break
        else:
                print("\t invalid choice")
    else:
        if current_user.name == "admin":
            print("\tthe option for admin")
            print("\t1:delete user account")
            print("\t2: see all user account")
            print("\t3: check total avaiable balance of bank")
            print("\t4: see total loan amount")
            print("\t5:off loan feature")
            print("\t6:on loan feature")
            print("\t7:Exit")
            choice = int(input("\t Enter your option : "))
            if(choice == 1):
                current_user.see_all_user(islami_bank)
                print("\t which account you want to delete enter this account_no : ")
                account_no = int(input("\t Enter account number : "))
                current_user.delete_user_account(account_no,islami_bank)
            elif choice == 2:
                current_user.see_all_user(islami_bank)
            elif choice == 3:
                current_user.total_balance(islami_bank)
            elif choice == 4:
                current_user.total_loan(islami_bank)
            elif choice == 5:
                current_user.off_loan(islami_bank)
            elif choice == 6:
                current_user.on_loan(islami_bank)
            elif choice == 7:
                current_user = None
            else:
                print("\t invalid choice")
        else:
            print("\tthe option for normal user")
            print("\t1:deposite amount")
            print("\t2: withdraw amount")
            print("\t3: check user available balance")
            print("\t4: see all transaction")
            print("\t5: take loan")
            print("\t6: transfer money")
            print("\t7:Exit")        
            choice = int(input("\t Enter your option : "))
            if(choice == 1):
                amount = int(input("\t Enter your amount : "))
                current_user.deposit(amount)
            elif choice == 2:
                amount = int(input("\t Enter your amount : "))
                current_user.withdraw(amount,islami_bank)
            elif choice == 3:
               current_user.check_balance()
            elif choice == 4:
                print(current_user.transaction_history)
            elif choice == 5:
                amount = int(input("\t Enter your amount : "))
                current_user.take_loan(islami_bank,amount)
            elif choice == 6:
                current_user.see_all_user(islami_bank)
                print("\t which account you want to transfer money enter this account_no : ")
                account_no = int(input("\tEnter your account number : "))
                amount = int(input("\t Enter your amount : "))
                current_user.transfer_balance(account_no,amount,islami_bank)
            elif choice == 7:
                current_user = None
            else:
                print("\t invalid choice")


                                                                      




