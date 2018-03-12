from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0
# Prompt the user for creating an account or access one

# Create a Savings account
class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccounts = {}
        #[key][0] => name; [key][1] => balance
    def createAccount(self, name, initialDeposit):
# Create 5 digit random number
        self.accountNumber = randint(10000, 99999)
# Make the random number as their account number
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account created successfully")
        print("Accoiunt number: ", self.accountNumber)

# Access an existing account
    def authenticate(self, name, accountNumber):
    # Accept their name
    # Accept the account number to validate
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print("Welcome: ", name)
                self.accountNumber = accountNumber
                return True
            else:
                print("Authencation failed: Wrong name")
                return False
        else:
            print("Authentication failed: Wrong account number")
            return False
    # Give options
    # Withdraw
    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawAmount
            print("Withdrawal successful")
            self.displayBalance()
    # Desposit
    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit successful")
        self.displayBalance()
    # Check Balance
    def displayBalance(self):
        print("Account balance: ", self.savingsAccounts[self.accountNumber][1])


savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access your account")
    print("Enter 3 to quit")
    userChoice = int(input())
    if userChoice is 1:
        print("Enter your name: ")
        name = input()
        print("Enter initial deposit: ")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    elif userChoice is 2:
        print("Enter your name: ")
        name = input()
        print("Enter account number: ")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display balance")
                print("Enter 4 to go back to previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    print("Enter withdrawal amount: ")
                    withdrawAmount = int(input())
                    savingsAccount.withdraw(withdrawAmount)
                elif userChoice is 2:
                    print("Enter the amount to  be deposited: ")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()
