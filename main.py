from core.manager import TransactionManager

from core.transaction import Transaction

from services.balance_service import BalanceService

from ui.menu import Menu

balance_service = BalanceService()
manager = TransactionManager()
menu = Menu()

while True:
    menu.show_menu()
    choice = menu.get_choice()
    if choice == "1":
        jumlah = int(input("Jumlah :"))
        kategori = input("Kategori :")
        catatan = input("Catatan :")
        pemasukan = Transaction(jumlah, kategori, catatan, "Pemasukan")
        manager.add_transaction(pemasukan)
        print("Pemasukan berhasil ditambah")
    elif choice == "2":
        jumlah = int(input("Jumlah :"))
        kategori = input("Kategori :")
        catatan = input("Catatan :")
        pengeluaran = Transaction(jumlah, kategori, catatan, "Pengeluaran")
        manager.add_transaction(pengeluaran)
        print("Pengeluaran berhasil ditambah")
    elif choice == "3":
        saldo = balance_service.calculate_balance(manager.transactions)
        print(f"Saldo sekarang:\nRp {saldo:,}")
    elif choice == "4":
        manager.show_transactions()
    elif choice == "0":
        print("keluar...")

        break
    else :
        print("Tidak valid!")