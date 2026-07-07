class BalanceService:
    def calculate_balance(self, transactions):
        saldo = 0
        for transaction in transactions:
            if transaction.jenis == "Pemasukan":
                saldo += transaction.amount
            elif transaction.jenis == "Pengeluaran":
                saldo -= transaction.amount
        return saldo
    
    def get_income(self, transactions):
        income = 0
        for transaction in transactions:
            if transaction.jenis == "Pemasukan":
                income += transaction.amount
        return income
    
    def get_expense(self, transactions):
        expense = 0
        for transaction in transactions:
            if transaction.jenis == "Pengeluaran":
                expense += transaction.amount
        return expense