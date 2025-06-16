import tkinter as tk

# Step 1: Simple Bank Account class
class BankAccount:
    def __init__(self):
        self.owner = "Dendup Dema"
        self.account_number = "216730055"
        self.balance = 500.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def top_up(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

# Step 2: Bank GUI using Tkinter
class BankApp:
    def __init__(self, root):
        self.account = BankAccount()

        root.title("Bank of Bhutan - Simple Banking App")

        # Title label
        tk.Label(root, text="🏦 Bank of Bhutan", font=("Arial", 16, "bold"), fg="dark green").pack(pady=5)

        # Display account info
        self.info = tk.Label(root, text=self.get_info(), font=("Arial", 10))
        self.info.pack(pady=5)

        # Input fields
        tk.Label(root, text="Enter Amount:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Label(root, text="Recipient (for Transfer):").pack()
        self.recipient_entry = tk.Entry(root)
        self.recipient_entry.pack()

        tk.Label(root, text="Phone Number (for Top-Up):").pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        # Buttons
        tk.Button(root, text="Deposit", width=20, command=self.deposit).pack(pady=3)
        tk.Button(root, text="Withdraw", width=20, command=self.withdraw).pack(pady=3)
        tk.Button(root, text="Transfer", width=20, command=self.transfer).pack(pady=3)
        tk.Button(root, text="Phone Top-Up", width=20, command=self.top_up).pack(pady=3)
        tk.Button(root, text="Delete / Clear Inputs", width=20, command=self.clear_fields).pack(pady=3)
        tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=10)

        # Message label
        self.message = tk.Label(root, text="", fg="blue")
        self.message.pack()

    # Display account info
    def get_info(self):
        return (f"Account Number: {self.account.account_number}\n"
                f"Account Holder: {self.account.owner}\n"
                f"Current Balance: Nu. {self.account.balance:.2f}")

    def update_info(self):
        self.info.config(text=self.get_info())

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                self.message.config(text="Enter a positive amount")
                return None
            return amount
        except:
            self.message.config(text="Invalid amount")
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
                self.message.config(text="Withdrawal successful")
            else:
                self.message.config(text="Not enough balance")
            self.update_info()

    def transfer(self):
        amount = self.get_amount()
        recipient = self.recipient_entry.get().strip()
        if not recipient:
            self.message.config(text="Please enter recipient name")
            return
        if amount:
            if self.account.transfer(amount):
                self.message.config(text=f"Transferred Nu.{amount:.2f} to {recipient}")
            else:
                self.message.config(text="Not enough balance")
            self.update_info()

    def top_up(self):
        amount = self.get_amount()
        phone = self.phone_entry.get().strip()
        if not phone:
            self.message.config(text="Please enter phone number")
            return
        if amount:
            if self.account.top_up(amount):
                self.message.config(text=f"Top-up of Nu.{amount:.2f} to {phone} successful")
            else:
                self.message.config(text="Not enough balance")
            self.update_info()

    def clear_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.recipient_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.message.config(text="Cleared all input fields")

# Step 3: Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()