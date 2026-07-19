from core.transaction import Transaction
from services.balance_service import BalanceService
import unittest

class TestBalanceService(unittest.TestCase):
    def setUp(self):
        self.service = BalanceService()
        self.transactions = [
            Transaction(10000, "Gaji", "Gaji Bulanan", "Pemasukan"),
            Transaction(5000, "Makan", "Ayam Geprek", "Pengeluaran"),
            Transaction(3000, "Bonus", "Bonus Game", "Pemasukan")
        ]
    def test_calculate_balance(self):
        saldo = self.service.calculate_balance(self.transactions)
        self.assertEqual(saldo, 8000)

    def test_get_income(self):
        income = self.service.get_income(self.transactions)
        self.assertEqual(income, 13000)

    def test_get_expense(self):
        expense = self.service.get_expense(self.transactions)
        self.assertEqual(expense, 5000)