import sqlite3
from core.transaction import Transaction
class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect("money_manager.db")
        self.cursor = self.connection.cursor()
        self.create_transaction_table() 

    def create_transaction_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount INTEGER,
                category TEXT,
                description TEXT,
                jenis TEXT
            )
        ''')
        self.connection.commit()

    def insert_transaction(self, transaction):
        self.cursor.execute('''
            INSERT INTO transactions(
                amount,
                category,
                description,
                jenis
            )
            VALUES(?, ?, ?, ?)
        ''',
        (transaction.amount,
        transaction.category,
        transaction.description,
        transaction.jenis)
        )
        self.connection.commit()

    def get_all_transactions(self):
        transactions = []
        self.cursor.execute("SELECT * FROM transactions")
        rows = self.cursor.fetchall()
        for row in rows:
            transaction = Transaction(row[1], row[2], row[3], row[4])
            transactions.append(transaction)
        return transactions