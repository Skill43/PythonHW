import logging

# Настройка логирования
logging.basicConfig(filename='atm.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        logging.info(f"Deposited ${amount}. New balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            logging.info(f"Withdrew ${amount}. New balance: ${self.balance}")
            return self.balance
        else:
            logging.error("Insufficient funds")
            return "Insufficient funds"

def main():
    account = BankAccount(1000)

    while True:
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            print("Current balance: $" + str(account.balance))
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            print("New balance: $" + str(account.deposit(amount)))
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            result = account.withdraw(amount)
            if type(result) == str:
                print(result)
            else:
                print("New balance: $" + str(result))
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()