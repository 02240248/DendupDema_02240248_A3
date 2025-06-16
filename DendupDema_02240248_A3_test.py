import unittest
from DendupDema_02240248_A3 import BankAccount, InvalidInputError, InsufficientFundsError

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Balance matches Part A (500 Nu.)
        self.account = BankAccount(owner="Dendup Dema", balance=500)
        self.recipient = BankAccount(owner="Demo Recipient", balance=200)

    def test_deposit_valid(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 600)

    def test_deposit_invalid(self):
        with self.assertRaises(InvalidInputError):
            self.account.deposit(-10)

    def test_withdraw_valid(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 200)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(1000)

    def test_transfer_valid(self):
        self.account.transfer(self.recipient, 150)
        self.assertEqual(self.account.balance, 350)
        self.assertEqual(self.recipient.balance, 350)

    def test_transfer_invalid_amount(self):
        with self.assertRaises(InvalidInputError):
            self.account.transfer(self.recipient, 0)

    def test_transfer_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.transfer(self.recipient, 600)

    def test_phone_top_up_valid(self):
        result = self.account.top_up_phone("77123456", 100)
        self.assertEqual(result, "Topped up Nu.100 to +975-77123456")
        self.assertEqual(self.account.balance, 400)

    def test_phone_top_up_invalid_number_length(self):
        with self.assertRaises(InvalidInputError):
            self.account.top_up_phone("1234", 50)

    def test_phone_top_up_invalid_number_prefix(self):
        with self.assertRaises(InvalidInputError):
            self.account.top_up_phone("88123456", 50)

    def test_phone_top_up_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.top_up_phone("77123456", 1000)

if __name__ == '__main__':
    unittest.main()
