class Menu:
    def show_menu(self):
        print("===== Money Manager =====")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Saldo")
        print("0. keluar")

    def get_choice(self):
        return input(">> ")