import json
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