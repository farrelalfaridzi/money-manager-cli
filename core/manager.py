from storage.database import DatabaseManager
from services.search_service import SearchService
from services.filter_service import FilterService
class TransactionManager:
    def __init__(self):
        self.database = DatabaseManager()
        self.transactions = self.database.get_all_transactions()
        self.service = SearchService()
        self.filter = FilterService()


    def add_transaction(self, transaction):
        self.database.insert_transaction(transaction)
        self.transactions.append(transaction)

    def show_transactions(self):
        if not self.transactions:
            print("tidak ada transaksi")
        else:
            for transaction in self.transactions:
                print(transaction)
                print("-------------------------")

    def delete_transaction(self, id):
        transaction = self.get_transaction_by_id(id)
        self.database.delete_transaction(id)
        self.transactions.remove(transaction)

    def update_transaction(self, id, amount, category, description, jenis):
        transaction = self.get_transaction_by_id(id)
        transaction.amount = amount
        transaction.category = category
        transaction.description = description
        transaction.jenis = jenis
        self.database.update_transaction(transaction)

    def get_transactions(self):
        return self.transactions

    def get_transaction_by_id(self, id):
        for transaction in self.transactions:
            if transaction.id == id:
                return transaction
        return None

    def search_transaction(self, category, jenis):
        if not category and jenis == "Semua":
            return self.transactions
        kategori = self.service.search_by_category(self.transactions, category)
        if jenis == "Semua":
            return kategori
        elif not category and jenis != "Semua":
            filter_transaksi = self.filter.filter_by_type(self.transactions, jenis)
            return filter_transaksi
        hasil = self.filter.filter_by_type(kategori, jenis)
        return hasil