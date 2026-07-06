class SearchService:
    def search_by_category(self, transactions, category):
        hasil = []
        for transaction in transactions:
            if transaction.category == category:
                hasil.append(transaction)
        return hasil