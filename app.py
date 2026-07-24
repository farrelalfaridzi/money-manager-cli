from flask import Flask, render_template, request, url_for, redirect
from core.transaction import Transaction
from core.manager import TransactionManager
from services.balance_service import BalanceService

app = Flask(__name__)

@app.route("/")
def home():
    manager = TransactionManager()
    balance_service = BalanceService()
    transactions = manager.get_transactions()
    saldo=balance_service.calculate_balance(transactions)
    pemasukan=balance_service.get_income(transactions)
    pengeluaran=balance_service.get_expense(transactions)
    recent_transactions = transactions[-5:]
    recent_transactions.reverse()
    return render_template("dashboard.html",
                            saldo=saldo,
                            pemasukan=pemasukan,
                            pengeluaran=pengeluaran,
                            recent_transactions=recent_transactions
                            )

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
        return redirect(url_for("transactions"))
    return render_template("add.html")

@app.route("/transactions")
def transactions():
    manager = TransactionManager()
    keyword = request.args.get("search", "")
    jenis = request.args.get("jenis")
    transactions = manager.search_transaction(keyword, jenis)
    return render_template(
        "transactions.html",
        transactions=transactions
    )

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    manager = TransactionManager()
    if request.method == "POST":
        jumlah = int(request.form["amount"])
        kategori = request.form["category"]
        catatan = request.form["description"]
        jenis = request.form["jenis"]
        manager.update_transaction(id, jumlah, kategori, catatan, jenis)
        return redirect(url_for("transactions"))
    return render_template("edit.html", transaction = manager.get_transaction_by_id(id))

@app.route("/delete/<int:id>")
def delete(id):
    manager = TransactionManager()
    manager.delete_transaction(id)
    return redirect(url_for("transactions"))

if __name__=="__main__":
    app.run(debug=True)