class FilterService:
    def filter_by_type(self, transactions, jenis):
        hasil = []
        for transaction in transactions:
            if transaction.jenis == jenis:
                hasil.append(transaction)
        return hasil