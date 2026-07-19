import unittest
from core.transaction import Transaction
from services.filter_service import FilterService

class TestFilterService(unittest.TestCase):
    def setUp(self):
        self.service = FilterService()
        self.transactions = [
            Transaction(10000, "Gaji", "Gaji Bulanan", "Pemasukan"),
            Transaction(5000, "Makan", "Ayam Geprek", "Pengeluaran"),
            Transaction(3000, "Bonus", "Bonus Game", "Pemasukan")
        ]

    def test_filter_service(self):
        hasil = self.service.filter_by_type(self.transactions, "Pemasukan")
        self.assertEqual(len(hasil), 2)
        self.assertEqual(hasil[0].jenis, "Pemasukan")
        self.assertEqual(hasil[1].jenis, "Pemasukan")