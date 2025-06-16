import tkinter as tk

# Custom error classes for clear error messages
class InvalidInputError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

# Basic BankAccount class
class BankAccount:
    def __init__(self, owner="Dendup Dema", balance=500):
        self.owner = owner
        self.account_number = "216730055"
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidInputError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidInputError("Amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough balance")
        self.balance -= amount

    def transfer(self, other_account, amount):
        if amount <= 0:
            raise InvalidInputError("Amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough balance")
        self.withdraw(amount)
        other_account.deposit(amount)

    def top_up_phone(self, phone_number, amount):
        # Check if phone number is valid Bhutan number
        if len(phone_number) != 8 or not phone_number.isdigit():
            raise InvalidInputError("Phone number must be 8 digits")
        if not phone_number.startswith(("77", "17", "71", "97")):
            raise InvalidInputError("Invalid Bhutan phone number")
        if amount <= 0:
            raise InvalidInputError("Amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough balance for top-up")
        self.balance -= amount
        return f"Topped up Nu.{amount} to +975-{phone_number}"

# GUI class to interact with user
class BankApp:
    def __init__(self, root):
        self.account = BankAccount()  # Create a bank account

        root.title("Bank of Bhutan - Simple Banking App")

        # Heading label
        tk.Label(root, text="🏦 Bank of Bhutan", font=("Arial", 16, "bold"), fg="green").pack(pady=5)

        # Account info label
        self.info = tk.Label(root, text=self.get_info(), font=("Arial", 10))
        self.info.pack(pady=5)

        # Entry fields and labels
        tk.Label(root, text="Enter Amount:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Label(root, text="Recipient Name (for Transfer):").pack()
        self.recipient_entry = tk.Entry(root)
        self.recipient_entry.pack()

        tk.Label(root, text="Phone Number (for Top-Up):").pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        # Buttons for each action
        tk.Button(root, text="Deposit", width=20, command=self.deposit).pack(pady=3)
        tk.Button(root, text="Withdraw", width=20, command=self.withdraw).pack(pady=3)
        tk.Button(root, text="Transfer", width=20, command=self.transfer).pack(pady=3)
        tk.Button(root, text="Phone Top-Up", width=20, command=self.top_up).pack(pady=3)
        tk.Button(root, text="Delete / Clear Inputs", width=20, command=self.clear_fields).pack(pady=3)
        tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=10)

        # Label to show messages to user
        self.message = tk.Label(root, text="", fg="blue")
        self.message.pack()

    def get_info(self):
        # Return string showing account info and balance
        return (f"Account Number: {self.account.account_number}\n"
                f"Account Holder: {self.account.owner}\n"
                f"Current Balance: Nu. {self.account.balance:.2f}")

    def update_info(self):
        # Update the account info label
        self.info.config(text=self.get_info())

    def get_amount(self):
        # Get amount from input and check it is valid
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise InvalidInputError("Enter a positive number")
            return amount
        except ValueError:
            raise InvalidInputError("Invalid amount")

    def deposit(self):
        try:
            amount = self.get_amount()
            self.account.deposit(amount)
            self.message.config(text="Deposit successful")
            self.update_info()
        except Exception as e:
            self.message.config(text=str(e))

    def withdraw(self):
        try:
            amount = self.get_amount()
            self.account.withdraw(amount)
            self.message.config(text="Withdrawal successful")
            self.update_info()
        except Exception as e:
            self.message.config(text=str(e))

    def transfer(self):
        try:
            amount = self.get_amount()
            recipient = self.recipient_entry.get().strip()
            if not recipient:
                raise InvalidInputError("Enter recipient name")
            dummy_account = BankAccount(owner=recipient, balance=0)
            self.account.transfer(dummy_account, amount)
            self.message.config(text=f"Transferred Nu.{amount:.2f} to {recipient}")
            self.update_info()
        except Exception as e:
            self.message.config(text=str(e))

    def top_up(self):
        try:
            amount = self.get_amount()
            phone = self.phone_entry.get().strip()
            message = self.account.top_up_phone(phone, amount)
            self.message.config(text=message)
            self.update_info()
        except Exception as e:
            self.message.config(text=str(e))

    def clear_fields(self):
        # Clear all input fields and message
        self.amount_entry.delete(0, tk.END)
        self.recipient_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.message.config(text="Inputs cleared")

# Start the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
