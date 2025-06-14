import tkinter as tk

# Simple Bank Account class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.mobile_balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def top_up_mobile(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.mobile_balance += amount
        return True

    def transfer(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

# GUI class
class BankAppGUI:
    def __init__(self, root):
        self.account = BankAccount("Dendup Dema", 300)
        self.root = root
        self.root.title("Simple Bank App")

        # Info label
        self.info = tk.Label(root, text=self.get_info())
        self.info.pack(pady=10)

        # Amount entry
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        # Recipient entry (for transfer)
        tk.Label(root, text="Recipient Account Number (for Transfer)").pack()
        self.recipient_entry = tk.Entry(root)
        self.recipient_entry.pack()

        # Buttons
        tk.Button(root, text="Deposit", command=self.deposit).pack(pady=2)
        tk.Button(root, text="Withdraw", command=self.withdraw).pack(pady=2)
        tk.Button(root, text="Top-Up Mobile", command=self.top_up).pack(pady=2)
        tk.Button(root, text="Transfer", command=self.transfer).pack(pady=2)

        # Message label
        self.message = tk.Label(root, text="")
        self.message.pack(pady=5)

    def get_info(self):
        return (f"Owner: {self.account.owner}\n"
                f"Balance: Nu. {self.account.balance:.2f}\n"
                f"Mobile Balance: Nu. {self.account.mobile_balance:.2f}")

    def update_info(self):
        self.info.config(text=self.get_info())

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                self.message.config(text="Enter a positive number")
                return None
            return amount
        except:
            self.message.config(text="Enter a valid number")
            return None

    def deposit(self):
        amount = self.get_amount()
        if amount:
            self.account.deposit(amount)
            self.message.config(text="Deposit successful")
            self.update_info()

    def withdraw(self):
        amount = self.get_amount()
        if amount:
            if self.account.withdraw(amount):
                self.message.config(text="Withdraw successful")
            else:
                self.message.config(text="Not enough balance")
            self.update_info()

    def top_up(self):
        amount = self.get_amount()
        if amount:
            if self.account.top_up_mobile(amount):
                self.message.config(text="Mobile top-up successful")
            else:
                self.message.config(text="Not enough balance")
            self.update_info()

    def transfer(self):
        amount = self.get_amount()
        recipient = self.recipient_entry.get().strip()
        if not recipient:
            self.message.config(text="Enter recipient account number")
            return
        if amount:
            if self.account.transfer(amount):
                self.message.config(text=f"Transferred Nu. {amount:.2f} to {recipient}")
            else:
                self.message.config(text="Not enough balance")
            self.update_info()

if __name__ == "__main__":
    root = tk.Tk()
    app = BankAppGUI(root)
    root.mainloop()
