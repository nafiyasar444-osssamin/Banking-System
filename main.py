import os

class BankAccount:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as file:
                for line in file:
                    name, balance = line.strip().split(",")
                    self.accounts[name] = float(balance)

    def save_accounts(self):
        with open("accounts.txt", "w") as file:
            for name, balance in self.accounts.items():
                file.write(f"{name},{balance}\n")

    def create_account(self):
        name = input("Enter Account Holder Name: ")

        if name in self.accounts:
            print("Account already exists!")
            return

        balance = float(input("Enter Initial Balance: "))
        self.accounts[name] = balance
        self.save_accounts()
        print("✅ Account Created Successfully!")

    def deposit(self):
        name = input("Enter Account Holder Name: ")

        if name not in self.accounts:
            print("❌ Account Not Found!")
            return

        amount = float(input("Enter Deposit Amount: "))
        self.accounts[name] += amount
        self.save_accounts()
        print("✅ Deposit Successful!")

    def withdraw(self):
        name = input("Enter Account Holder Name: ")

        if name not in self.accounts:
            print("❌ Account Not Found!")
            return

        amount = float(input("Enter Withdraw Amount: "))

        if amount > self.accounts[name]:
            print("❌ Insufficient Balance!")
        else:
            self.accounts[name] -= amount
            self.save_accounts()
            print("✅ Withdraw Successful!")

    def check_balance(self):
        name = input("Enter Account Holder Name: ")

        if name in self.accounts:
            print(f"Current Balance: {self.accounts[name]} Tk")
        else:
            print("❌ Account Not Found!")

    def show_all_accounts(self):
        if len(self.accounts) == 0:
            print("No Accounts Found.")
        else:
            print("\n------ All Accounts ------")
            for name, balance in self.accounts.items():
                print(f"{name} : {balance} Tk")


bank = BankAccount()

while True:
    print("\n========== Bank Management System ==========")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.deposit()

    elif choice == "3":
        bank.withdraw()

    elif choice == "4":
        bank.check_balance()

    elif choice == "5":
        bank.show_all_accounts()

    elif choice == "6":
        print("Thank You ❤️")
        break

    else:
        print("Invalid Choice!")
