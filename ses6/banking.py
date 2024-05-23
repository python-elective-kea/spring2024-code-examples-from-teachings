class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

class Account:
    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer  # This should be a Customer object
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
        else:
            print("The object being added is not an Account.")

# Example usage
customer1 = Customer("John Doe", "john.doe@example.com")
account1 = Account("12345", customer1, 1000)

bank = Bank()
bank.add_account(account1)

print(f"Bank has {len(bank.accounts)} account(s).")
for account in bank.accounts:
    print(f"Account Number: {account.account_number}, Customer: {account.customer.name}, Balance: {account.balance}")

    