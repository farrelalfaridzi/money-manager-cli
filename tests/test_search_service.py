import unittest
from core.transaction import Transaction
from services.search_service import SearchService

class TestSearchService(unittest.TestCase):
    def setUp(self):
        self.service = SearchService()
        self.transactions = [
            Transaction(10000, "Gaji", "Gaji Bulanan", "Pemasukan"),
            Transaction(5000, "Makan", "Ayam Geprek", "Pengeluaran"),
            Transaction(3000, "Bonus", "Bonus Game", "Pemasukan")
        ]

    def test_search_by_category(self):
        hasil = self.service.search_by_category(self.transactions, "Makan")
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0].category, "Makan")
        self.assertEqual(hasil[0].amount, 5000)