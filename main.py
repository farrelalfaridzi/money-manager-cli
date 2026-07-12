from core.manager import TransactionManager

from core.transaction import Transaction

from services.balance_service import BalanceService

from ui.menu import Menu

from services.search_service import SearchService

from services.filter_service import FilterService

from storage.file_manager import FileManager

balance_service = BalanceService()
manager = TransactionManager()
menu = Menu()
search_service = SearchService()
filter_service = FilterService()
file_manager = FileManager()

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
    elif choice == "5":
        kategori = input("Kategori : ")
        transactions = search_service.search_by_category(manager.transactions, kategori)
        if not transactions:
            print("Tidak ada transaksi")
        else:
            for transaction in transactions:
                print(transaction)
                print("--------------------")
    elif choice == "6":
        jenis = input("Masukan Jenis \n(Pemasukan/Pengeluaran) : ")
        transaction_by_jenis = filter_service.filter_by_type(manager.transactions, jenis)
        if not transaction_by_jenis:
            print("Tidak ada transaksi")
        else:
            for transaction in transaction_by_jenis:
                print(transaction)
                print("--------------------")
    elif choice == "7":
        choice_7 = input("Pemasukan/Pengeluaran : ")
        if choice_7 == "Pemasukan":
            pemasukan_7 = balance_service.get_income(manager.transactions)
            print(f"Total Pemasukan : Rp {pemasukan_7:,}")
        elif choice_7 == "Pengeluaran":
            pengeluaran_7 = balance_service.get_expense(manager.transactions)
            print(f"Total Pengeluaran : Rp {pengeluaran_7:,}")
        else:
            print("Tidak valid")
    elif choice == "8":
        file_manager.save(manager.transactions)
        print("Data berhasil disimpan")
    elif choice == "9":
        loaded_transactions = file_manager.load()
        print("Data berhasil dimuat")
        for transaction in loaded_transactions :
            manager.add_transaction(transaction)
    elif choice == "0":
        print("keluar...")

        break
    else :
        print("Tidak valid!")