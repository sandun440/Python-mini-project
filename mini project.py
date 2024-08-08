#create class name as Bank
class Bank:

    #define the dictionary
    def __init__(self):
        self.bank_details = {}

    #define the menu
    def menu(self):                         #print menu option
        print()
        print("### Enter number [1] to Create a account")
        print("### Enter number [2] to Check balance")
        print("### Enter number [3] to Deposit money")
        print("### Enter number [4] to money Withdrawal")
        print("### Enter number [5] to Transfer money")
        print("### Enter any other number to \"Exit\" ")
        print()
                                     #define create funtion
    def create_acc(self):
        from random import randrange               # create account number -- random
        acc_num = randrange(10000, 99999)
        balance = float(input("Enter the first deposit amount: "))

        if(acc_num in self.bank_details):
            print("----------------------------------------------")
            print("\nThis account is already have !")
            print("\n----------------------------------------------")
        else:
            self.acc = acc_num
            self.bal = balance

            if(self.bal <= 0):
                print("\nPlease enter the positive amount!")
            else:
             self.bank_details[self.acc] = self.bal

             print("\nYou have successfully created an account.")
             print("----------------------------------------------")
             print("|    Your Account Number is: ", self.acc)
             print("|    Balance: RS.{:.2f}".format(self.bal))
             print("----------------------------------------------")


                        #define balance funtion
    def balance(self):
        acc_num = int(input("Enter your account number: "))
        self.acc = acc_num
        if (self.acc not in self.bank_details):
            print("\nThis account is not existing!")
        else:
            self.bal = self.bank_details.get(self.acc)
            print("----------------------------------------------")
            print("\nYour balance: RS.{:.2f}".format(self.bal))
            print("\n----------------------------------------------")

                    #define deposit function
    def deposit(self):
         acc_num = int(input("Enter your account number: "))
         self.acc = acc_num
         if (self.acc not in self.bank_details):
             print("----------------------------------------------")
             print("\nThis account is not existing!")
             print("\n----------------------------------------------")
         else:
          deposit = float(input("Enter the deposit amount: "))
          self.dep = deposit

         if(self.dep <= 0):
             print("----------------------------------------------")
             print("\nPlease enter the positive value!")
             print("\n----------------------------------------------")
         else:
             self.new_balance = self.bal + self.dep
             self.bal = self.new_balance
             self.bank_details[self.acc] = self.bal
             print("----------------------------------------------")
             print("\nMoney deposit successfully")
             print("Your balance: RS.{:.2f}".format(self.bal))
             print("\n----------------------------------------------")

                #define withdrawl function
    def withdrawl(self):
        accno = int(input("Enter your account number: "))
        self.acc = accno
        balance = self.bank_details.get(self.acc)
        self.withdrawl_balance = balance

        if (self.acc not in self.bank_details):
            print("----------------------------------------------")
            print("This account is not existing!")
            print("\n----------------------------------------------")
        else:
            with_deposit = float(input("Enter the withdrawal amount: "))
            self.dep = with_deposit

        if(self.dep < 0):
            print("----------------------------------------------")
            print("\nPlease enter a positive value")
            print("\n----------------------------------------------")
        elif(self.dep > self.bal):
            print("----------------------------------------------")
            print("\nYou doesn't have sufficient balance!")
            print("\n----------------------------------------------")

        else:
            self.bal = self.withdrawl_balance - self.dep
            self.bank_details[self.acc] = self.bal
            print("----------------------------------------------")
            print("\nMoney withdrawal successfully")
            print("Balance: Rs.{:.2f}".format(self.bal))
            print("\n----------------------------------------------")

                    #define transfer funtion
    def money_transfer(self):
        acc_no = int(input("Enter your account number: "))
        self.acc = acc_no
        balance = self.bank_details.get(self.acc)
        self.transfer_balance = balance
        if (self.acc not in self.bank_details):
            print("----------------------------------------------")
            print("\nThis account is not existing!")
            print("\n----------------------------------------------")
        else:
            rec_cno = int(input("Enter a receiver account number: "))
            self.rev = rec_cno
            if (self.rev not in self.bank_details):
                print("----------------------------------------------")
                print("\nThis account is not existing!")
                print("\n----------------------------------------------")
            else:
                tr_amount = float(input("Enter a transfer amount: "))
                self.tra_amount = tr_amount

                if(self.tra_amount <= 0):
                    print("----------------------------------------------")
                    print("\nPlease enter a positive value!")
                    print("\n----------------------------------------------")
                elif(self.tra_amount > self.transfer_balance):
                    print("----------------------------------------------")
                    print("\nYou doesn't have sufficient balance!")
                    print("\n----------------------------------------------")
                else:
                    sender = self.bank_details.get(self.acc)            #Get the reciever's balance from "bank_details" and assign into "sender"
                    self.sen_dels = sender
                    self.sen_dels = self.sen_dels - self.tra_amount
                    self.bal = self.sen_dels

                    self.bank_details[self.acc] = self.bal               #Update reciever's balance
                    print("----------------------------------------------")
                    print("\nYour Account Balance: RS.{:.2f}".format(self.bal))
                    print("Transfer amount: RS.{:.2f}".format(self.tra_amount))

                    m_recev = self.bank_details.get(self.rev)
                    self.rev_dels = m_recev
                    self.rev_dels = self.rev_dels + self.tra_amount
                    self.bal = self.rev_dels

                    self.bank_details[self.rev] = self.bal
                    print("Money transfer successfully")
                    print("\n----------------------------------------------")
    def main(self):                         #Create a function as main
        while True:                         #Calling Execute "menu,create,balance,deposit,withdrawal and transfer" functions while loop when break
            bank.menu()
            choice = int(input("Enter your choice: "))

            if (choice == 1):
                bank.create_acc()
            elif (choice == 2):
                bank.balance()
            elif (choice == 3):
                bank.deposit()
            elif (choice == 4):
                bank.withdrawl()
            elif (choice == 5):
                bank.money_transfer()
            else:
                print("----------------------------------------------")
                print("\nExit!")
                print("\n----------------------------------------------")
                break                                       #This is the point while loops is false

bank = Bank()                   #Assign "Bank" class to "bank" object
bank.main()                     #Calling "main" function by using object