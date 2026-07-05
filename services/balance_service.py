class BalanceService:
    def calculate_balance(self, transactions):
        saldo = 0
        for transaction in transactions:
            if transaction.jenis == "Pemasukan":
                saldo += transaction.amount
            elif transaction.jenis == "Pengeluaran":
                saldo -= transaction.amount
        return saldo