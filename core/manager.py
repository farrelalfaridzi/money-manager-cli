from storage.database import DatabaseManager
class TransactionManager:
    def __init__(self):
        self.database = DatabaseManager()
        self.transactions = self.database.get_all_transactions()

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