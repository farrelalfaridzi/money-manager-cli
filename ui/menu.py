class Menu:
    def show_menu(self):
        print("===== Money Manager =====")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Saldo")
        print("4. Lihat Semua Transaksi")
        print("5. Cari berdasarkan kategori")
        print("6. Filter berdasarkan jenis")
        print("7. Lihat total Pemasukan/Pengeluaran")
        print("0. keluar")

    def get_choice(self):
        return input(">> ")