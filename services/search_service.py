class SearchService:
    def search_by_category(self, transactions, category):
        hasil = []
        for transaction in transactions:
            if category.lower() in transaction.category.lower():
                hasil.append(transaction)
        return hasil