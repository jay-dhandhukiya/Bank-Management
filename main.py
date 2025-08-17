import json
import random
from pathlib import Path

class Bank:
     try:
          Database = "data.json"
          Data = []
          if Path(Database).exists():
               with open(Database, "r") as file:
                    Data = json.load(file)
          else:
               print("No Such File Found....")
     except Exception as err:
          print(f"An Error Occured: {err}")
     
     # Update the Database File
     @classmethod         
     def __update(cls):
          with open(cls.Database, "w") as file:
               file.write(json.dumps(Bank.Data))
     
     # Generate Random Account Number
     @classmethod
     def __AccountNumber(cls):
          return random.randint(1000000000, 9999999999)
     
     def CreateAccount(self):
          info = {
               "name": input("Enter your name: "),
               "age": int(input("Enter your age: ")),
               "email": input("Enter your email: "),
               "pin": input("Enter your 6 digits pin: "),
               "account_number": Bank.__AccountNumber(),
               "balance": 0
          }
          if info["age"] < 18 or len(str(info["pin"])) != 6:
               print("You are not Created an Account as you are not eligible for this service.")
          else:
               print("Account Created Successfully...")
               for i in info:
                    print(f"{i}: {info[i]}")
               print("Please Write Down Your Account Number...")
               Bank.Data.append(info)
               Bank.__update()

     def DepositAmount(self):
          AccountNumber = int(input("Enter your Account Number: "))
          Pin = input("Enter your 6 digits pin: ")

          userData =[ i for i in Bank.Data if i["account_number"] == AccountNumber and i["pin"] == Pin]

          if userData == False:
               print("Invalid Account Number or Pin")
          else:
               Amount = int(input("Enter the Amount: "))
               if Amount > 10000 or Amount < 0:
                    print("Amount should be between 0 and 10000")
               else:
                    userData[0]["balance"] += Amount
                    Bank.__update()
                    print("Amount Deposited Successfully...")

     def WithdrawAmount(self):
          AccountNumber = int(input("Enter your Account Number: "))
          Pin = input("Enter your 6 digits pin: ")

          userData =[ i for i in Bank.Data if i["account_number"] == AccountNumber and i["pin"] == Pin]

          if userData == False:
               print("Invalid Account Number or Pin")
          else:
               Amount = int(input("Enter the Withdraw Amount: "))
               if userData[0]["balance"] < Amount or Amount < 0:
                    print("Insufficient Balance or Invalid Amount Entered ...")
               else:
                    userData[0]["balance"] -= Amount
                    Bank.__update()
                    print("Amount Withdrawn Successfully...")

     def Details(self):
          AccountNumber = int(input("Enter your Account Number: "))
          Pin = input("Enter your 6 digits pin: ")

          userData =[ i for i in Bank.Data if i["account_number"] == AccountNumber and i["pin"] == Pin]
          print("Your Details are: ")
          for i in userData[0]:
               print(f"{i}: {userData[0][i]}")
          
     def UpdateDetails(self):
          AccountNumber = int(input("Enter your Account Number: "))
          Pin = input("Enter your 6 digits pin: ")

          userData =[ i for i in Bank.Data if i["account_number"] == AccountNumber and i["pin"] == Pin]
          if not userData:
               print("Invalid Account Number or Pin")
          else:
               print("We can Update your Name, Email and Pin only and no change than skipping ...")
               newData = {
                    "name": input("Enter your name or press enter to skip: "),
                    "email": input("Enter your email or press enter to skip: "),
                    "pin": input("Enter your 6 digits pin or press enter to skip: ")
               }

               if len(str(newData["pin"])) != 6 and newData["pin"] != "":
                    print("Pin should be 6 digits only...")
                    return

               if newData["name"] == "" :
                    newData["name"] = userData[0]['name']
               if newData["email"] == "":
                    newData["email"] = userData[0]['email']
               if newData["pin"] == "":
                    newData["pin"] = userData[0]['pin']
               
               newData['age'] = userData[0]["age"]
               newData['account_number'] = userData[0]["account_number"]
               newData['balance'] = userData[0]["balance"]

               for i in newData:
                    if newData[i] == userData[0][i]:
                         continue
                    else:
                         userData[0][i] = newData[i]

               Bank.__update()

               print("Details Updated Successfully...")

     def DeleteAccount(self):
          AccountNumber = int(input("Enter your Account Number: "))
          Pin = input("Enter your 6 digits pin: ")

          userData =[ i for i in Bank.Data if i["account_number"] == AccountNumber and i["pin"] == Pin]
          if not userData:
               print("Invalid Account Number or Pin")
          else:
               Bank.Data.remove(userData[0])
               Bank.__update()
               print("Account Deleted Successfully...")

# Object Creation
User = Bank()

print("press 1 for Creating an Account")
print("press 2 for Depositing the Money in the bank")
print("press 3 for Withdrawing the Money")
print("press 4 for Details")
print("press 5 for Updating the Details")
print("press 6 for Deleting the Account")

choice = int(input("Enter your choice: "))

if choice == 1:
     User.CreateAccount()

if choice == 2:
     User.DepositAmount()

if choice == 3:
     User.WithdrawAmount()

if choice == 4:
     User.Details()

if choice == 5:
     User.UpdateDetails()

if choice == 6:
     User.DeleteAccount()