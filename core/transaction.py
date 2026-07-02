class Transaction:
    def __init__(self, amount, category, description, jenis):
        self.amount = amount
        self.category = category
        self.jenis = jenis
        self.description = description

    def __str__(self):
        return(f"Kategori : {self.category}\nJumlah   : Rp{self.amount:,}\nJenis    : {self.jenis}\nCatatan  : {self.description}")

t = Transaction(2500,"[makanan]","baso","pengeluaran")
print(t)