from flask import Flask, render_template, request
from core.transaction import Transaction
from core.manager import TransactionManager

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    manager = TransactionManager()
    if request.method == "POST":
        jumlah = int(request.form["amount"])
        kategori = request.form["category"]
        catatan = request.form["description"]
        jenis = request.form["jenis"]
        transaction = Transaction(jumlah, kategori, catatan, jenis)
        manager.add_transaction(transaction)
    return render_template("add.html")

@app.route("/transactions")
def transactions():
    manager = TransactionManager()
    return render_template("transactions.html",
                            transactions = manager.get_transactions())

if __name__=="__main__":
    app.run(debug=True)