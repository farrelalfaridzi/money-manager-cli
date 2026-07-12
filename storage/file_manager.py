import json
from core.transaction import Transaction
class FileManager:
    def save(self, transactions):
        data_list = []
        for transaction in transactions:
            transaction_data = {
                "amount":transaction.amount,
                "category":transaction.category,
                "jenis":transaction.jenis,
                "description": transaction.description
            }
            data_list.append(transaction_data)
        with open("save.json", "w") as file :
            json.dump(data_list, file, indent=4)

    def load(self):
        with open("save.json", "r") as file:
            data = json.load(file)
            if not data:
                return []
            transactions = []
            for item in data:
                t = Transaction(item["amount"], item["category"], item["description"], item["jenis"])
                transactions.append(t)
            return transactions