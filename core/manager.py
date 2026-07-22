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

    def delete_transaction(self, nomor):
        nomor -= 1
        transaction = self.transactions[nomor]
        id = transaction.id
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