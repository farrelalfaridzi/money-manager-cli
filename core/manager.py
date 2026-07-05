class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def show_transactions(self):
        if not self.transactions:
            print("tidak ada transaksi")
        else:
            for transaction in self.transactions:
                print(transaction)
                print("-------------------------")