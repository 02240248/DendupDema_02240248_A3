import unittest

# Simple BankAccount class for testing
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.active = True

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Not enough money")
        self.balance -= amount

    def transfer(self, amount, other_account):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Invalid account to transfer to")
        self.withdraw(amount)
        other_account.deposit(amount)

    def delete_account(self):
        if self.balance != 0:
            raise Exception("Cannot delete account with money")
        self.active = False

    def phone_topup(self, phone_number, amount):
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError("Phone number must have 10 digits")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Not enough money for top-up")
        self.balance -= amount
        return f"Top-up of {amount} to {phone_number} successful."

# Unit test class to check the BankAccount class
class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # This runs before each test
        self.acc1 = BankAccount(1000)
        self.acc2 = BankAccount(500)

    # Test for wrong deposit amount
    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.acc1.deposit(-100)

    # Test withdraw zero money
    def test_withdraw_zero(self):
        with self.assertRaises(ValueError):
            self.acc1.withdraw(0)

    # Test top-up with bad phone number
    def test_topup_bad_number(self):
        with self.assertRaises(ValueError):
            self.acc1.phone_topup("1234abc", 50)

    # Test top-up with negative amount
    def test_topup_negative_amount(self):
        with self.assertRaises(ValueError):
            self.acc1.phone_topup("0123456789", -20)

    # Test transfer to wrong type
    def test_transfer_wrong_account(self):
        with self.assertRaises(TypeError):
            self.acc1.transfer(100, "not_an_account")

    # Test withdraw more money than balance
    def test_withdraw_too_much(self):
        with self.assertRaises(ValueError):
            self.acc1.withdraw(2000)

    # Test delete account when balance is not zero
    def test_delete_account_with_money(self):
        with self.assertRaises(Exception):
            self.acc1.delete_account()

    # Test successful deposit
    def test_deposit_success(self):
        self.acc1.deposit(200)
        self.assertEqual(self.acc1.balance, 1200)

    # Test successful withdraw
    def test_withdraw_success(self):
        self.acc1.withdraw(500)
        self.assertEqual(self.acc1.balance, 500)

    # Test successful transfer
    def test_transfer_success(self):
        self.acc1.transfer(300, self.acc2)
        self.assertEqual(self.acc1.balance, 700)
        self.assertEqual(self.acc2.balance, 800)

    # Test successful account deletion
    def test_delete_account_success(self):
        self.acc1.withdraw(1000)  # Make balance zero
        self.acc1.delete_account()
        self.assertFalse(self.acc1.active)

    # Test successful phone top-up
    def test_phone_topup_success(self):
        result = self.acc1.phone_topup("0123456789", 100)
        self.assertEqual(result, "Top-up of 100 to 0123456789 successful.")
        self.assertEqual(self.acc1.balance, 900)

if __name__ == "__main__":
    unittest.main()
