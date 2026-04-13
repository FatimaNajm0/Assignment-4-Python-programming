class BankAccount:
    def __init__(self, customer_name, account_no, initial_balance):
        self.customer_name = customer_name
        self.account_no = account_no
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print("Withdraw successful!")
        else:
            print("Insufficient balance!")

    def balance(self):
        print(f"Current Balance: ${self.account_balance}")

my_account = BankAccount("Fatima", "10203040", 500)

while True:
    print("\n--- Menu ---")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance inquiry")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter amount to withdraw: "))
        my_account.withdraw(amount)
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        my_account.deposit(amount)
    elif choice == '3':
        my_account.balance()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
