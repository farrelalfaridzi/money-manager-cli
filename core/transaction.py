class Transaction:
    def __init__(self, amount, category, description, jenis, id=None):
        self.amount = amount
        self.category = category
        self.jenis = jenis
        self.description = description
        self.id = id

    def __str__(self):
        return(f"Kategori : {self.category}\nJumlah   : Rp{self.amount:,}\nJenis    : {self.jenis}\nCatatan  : {self.description}")