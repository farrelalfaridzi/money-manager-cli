# 💰 Money Manager CLI

A command-line personal finance management application built with Python. This project allows users to record income and expenses, calculate balances, search and filter transactions, and manage financial records using SQLite as the database.

The project was developed as a learning journey to practice Object-Oriented Programming (OOP), software architecture, database integration, Git workflow, and unit testing.

---

## ✨ Features

- ➕ Add Income
- ➖ Add Expense
- 💰 Calculate Current Balance
- 📜 View Transaction History
- 🔍 Search Transactions by Category
- 🏷️ Filter Transactions by Type
- 📈 View Total Income
- 📉 View Total Expense
- 🗑️ Delete Transaction
- ✏️ Update Transaction
- 💾 Persistent Storage using SQLite
- ✅ Unit Testing

---

## 🛠️ Tech Stack

- Python 3
- SQLite3
- unittest
- Git & GitHub

---

## 📁 Project Structure

```
money-manager-cli/
│
├── core/
│   ├── manager.py
│   └── transaction.py
│
├── services/
│   ├── balance_service.py
│   ├── filter_service.py
│   └── search_service.py
│
├── storage/
│   └── database.py
│
├── data/
│   └── money_manager.db
│
├── tests/
│   ├── test_balance_service.py
│   ├── test_filter_service.py
│   └── test_search_service.py
│
├── ui/
│   └── menu.py
│
├── main.py
└── README.md
```

---

## 🚀 Installation

Clone this repository.

```bash
git clone https://github.com/farrelalfaridzi/money-manager-cli.git
```

Move into the project directory.

```bash
cd money-manager-cli
```

Run the application.

```bash
python main.py
```

---

## 📸 Preview

Example menu:

```text
========== Money Manager ==========

1. Add Income
2. Add Expense
3. Show Balance
4. Show Transactions
5. Search by Category
6. Filter by Type
7. Show Total Income / Expense
8. Delete Transaction
9. Update Transaction
0. Exit
```

---

## 🧪 Running Tests

Run all unit tests using:

```bash
python -m unittest discover
```

---

## 📚 What I Learned

During this project I learned:

- Object-Oriented Programming (OOP)
- Layered Project Architecture
- SQLite Database Integration
- CRUD Operations
- Exception Handling
- Git Branching & Merge Workflow
- Unit Testing with unittest
- Clean Code Refactoring

---

## 🔮 Future Improvements

- Monthly financial reports
- Budget planning
- Data visualization
- Export to CSV / Excel
- User authentication
- Flask REST API
- Web Interface

---

## 👨‍💻 Author

**Muhamad Farrel Alfaridzi**

GitHub:
https://github.com/farrelalfaridzi