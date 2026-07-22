# 💰 Money Manager

A personal finance management application built with Python.

This project started as a command-line (CLI) application and is gradually evolving into a full-featured web application using Flask.

The main goal of this project is not only to build a finance manager, but also to document the complete learning journey from Python fundamentals to software engineering, web development, and backend development.

---

## ✨ Features

### 💻 CLI Version (v1.0)

- ➕ Add Income
- ➖ Add Expense
- 💰 Calculate Balance
- 📜 View Transactions
- 🔍 Search Transactions
- 🏷️ Filter Transactions
- 📈 Monthly Report
- ✏️ Update Transaction
- 🗑️ Delete Transaction
- 💾 SQLite Storage
- ✅ Unit Testing

---

### 🌐 Web Version (v2.0 - In Progress)

#### Flask Fundamentals

- ✅ Flask Setup
- ✅ Routing
- ✅ HTML Templates
- ✅ Template Inheritance
- ✅ Jinja2
- ✅ Forms
- ✅ GET & POST
- ✅ Input Validation

#### Core Features

- ✅ Add Transaction
- ✅ View Transactions
- ✅ Edit Transaction
- ✅ Delete Transaction
- 🚧 Dashboard
- 🚧 Search
- 🚧 Filter
- 🚧 Category
- 🚧 Monthly Report

---

## 🛠️ Tech Stack

- Python
- Flask
- SQLite3
- HTML
- Jinja2
- unittest
- Git
- GitHub

---

## 📁 Project Structure

```text
money-manager-cli/
│
├── core/
│   ├── manager.py
│   └── transaction.py
│
├── storage/
│   └── database.py
│
├── services/
│   ├── balance_service.py
│   ├── filter_service.py
│   └── search_service.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   └── transactions.html
│
├── static/
│
├── tests/
│
├── data/
│
├── app.py
├── main.py
└── README.md
```

---

## 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/farrelalfaridzi/money-manager-cli.git
```

Enter the project.

```bash
cd money-manager-cli
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

### Run CLI Version

```bash
python main.py
```

---

### Run Web Version

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## 🧪 Running Tests

```bash
python -m unittest discover
```

---

# 🚀 Roadmap

## ✅ v1.0 — CLI Application

- Transaction Class (OOP)
- Income & Expense
- Balance Calculation
- Search
- Filter
- Category
- Monthly Report
- SQLite Storage
- Unit Testing
- Documentation
- Git Workflow
- Release v1.0

---

## 🚧 v2.0 — Flask Web Application

### Flask Fundamentals

- [x] Flask Setup
- [x] Routing
- [x] HTML
- [ ] CSS
- [x] Template Inheritance
- [x] Jinja2
- [x] Form
- [x] GET & POST
- [x] request.form
- [x] Input Validation

### Dashboard

- [ ] Dashboard Summary
- [ ] Balance
- [ ] Total Income
- [ ] Total Expense

### Core Features

- [x] SQLite Integration
- [x] Add Transaction
- [x] View Transactions
- [x] Edit Transaction
- [x] Delete Transaction
- [ ] Search
- [ ] Filter
- [ ] Category
- [ ] Monthly Report

### Visualization

- [ ] Charts
- [ ] Export CSV
- [ ] Import CSV
- [ ] Database Backup

### User

- [ ] Login
- [ ] Logout
- [ ] Multi User

- [ ] Release v2.0

---

## 🔮 v3.0 — Modern Backend

### AI Features

- [ ] AI Financial Analysis
- [ ] Spending Recommendation
- [ ] Financial Insight

### API

- [ ] FastAPI
- [ ] REST API
- [ ] API Documentation

### Deployment

- [ ] Docker
- [ ] Deploy
- [ ] Domain
- [ ] CI/CD

- [ ] Release v3.0

---

## 📚 Learning Journey

During this project, I have learned:

- Object-Oriented Programming (OOP)
- Layered Project Architecture
- SQLite Database
- CRUD Operations
- Flask Fundamentals
- Jinja2 Templates
- Routing & Forms
- Git Branch Workflow
- Unit Testing
- Clean Code & Refactoring

This repository will continue to grow as I learn more about backend development, web development, software engineering, and AI.

---

## 👨‍💻 Author

**Muhamad Farrel Alfaridzi**

GitHub

https://github.com/farrelalfaridzi