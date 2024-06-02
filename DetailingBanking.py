# Requirements:-

# 1. New Account creation
# 2. Modify Existing account
# 3. Change phone number
# 4. Withdraw
# 5. Balance Enquiry
# 6. Deposit ammount

import pickle

import pathlib

import os

class Account:

    def basicDetails(self):

        self.accountHolderName = ""

        self.accountNumber = 0

        self.deposit = 0

        self.phoneNo = 0

        self.accountType = ""

    def createAccount(self):

        self.accountHolderName = str(input("Enter your name: "))

        self.accountNumber = str(input("Enter your Account Number: "))

        self.deposit = str(input("Enter money to deposit: "))

        self.phoneNo = str(input("Enter your phone number: "))

        self.accountType = str(input("Enter your Account type [Saving/ Current]: "))

    def showAcc(self):

        print("Your name is: ", self.accountHolderName)

        print("Your account number is: ", self.accountNumber)

        print("Your phone number is: ", self.phoneNo)

        print("Your account type is: ", self.accountType)

    def modifyAccount(self):

        self.existingAccNum = print("Enter your existing account number: ")
        self.accountNumber = self.existingAccNum
        print(f"Your modified account number is {self.accountNumber}")

    def modifyPhoneNumber(self):

        self.existingPhnNo = print("Enter your existing Phone number: ")
        self.phoneNo = self.existingPhnNo
        print(f"Your modified phone number is {self.phoneNo}")

    def withdrawal(self):

        self.withdrawalAmm = print ("Enter the amount you want to withdraw")
        self.deposit = self.deposit - self.withdrawalAmm
        self.balance = ("Please select 1 if you want to see the balance")
        if self.balance == 1:
            print(f"Your account balance is {self.deposit}")
        else:
            print("Thanks for the Withdrawal")




def intro():

   print("\t\t\t\t**********************")

   print("\t\t\t\tBANK MANAGEMENT SYSTEM")

   print("\t\t\t\t**********************")

   print("\t\t\t\tBrought To You By:")

   print("\t\t\t\tprojectworlds.in")

   input()

def writeAccount():
       
    account = Account
    account.basicDetails(Account)
    account.createAccount(Account)
    account.showAcc(Account)

# Start the program
intro()

drop= writeAccount()

def displayAll():

    file = pathlib.Path("accounts.data")

    if file.exists ():

       infile = open("accounts.data","rb")

       mylist = pickle.load(infile)

       for item in mylist :

           print(item.accNo," ", item.name, " ",item.type, " ",item.deposit)

       infile.close()

    else :

        nfile = open("accounts.data", "wb")

        mlist = pickle.dump(nfile)

        for item in mlist:
           
           print(item.accNo," ", item.name, " ",item.type, " ",item.deposit)

        nfile.close()

displayAll()

# def call():
#     with open("accountData.pickle", "rb") as f:
#         loadedObject = pickle.load(f)
#         print(loadedObject)
# call()

        








    



