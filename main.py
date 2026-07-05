from core.manager import TransactionManager

from core.transaction import Transaction

from services.balance_service import BalanceService

t = Transaction(20000, "Kebutuhan", "Bensin", "Pengeluaran")
t2 = Transaction(50000, "Makanan", "Nasi goreng", "Pengeluaran")
service = BalanceService()
transaction_manager = TransactionManager()
transaction_manager.add_transaction(t)
transaction_manager.add_transaction(t2)
transaction_manager.show_transactions()
saldo = service.calculate_balance(transaction_manager.transactions)
print(saldo)