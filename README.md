# Inventory Management System (Backend API)

A RESTful API built with **Python (Flask)** and **MySQL** to manage product inventory. This system supports Create, Read, and Search operations and uses environment variables for security.

## 🚀 Features
* **REST API:** Endpoints to add products, view all items, and search by name.
* **Database Integration:** Persistent storage using MySQL.
* **Security:** Uses `.env` for safe credential management (dotenv).
* **Search Logic:** SQL `LIKE` operator for pattern matching.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** Flask
* **Database:** MySQL (PyMySQL driver)
* **Tools:** Git, Postman (for testing)

## 📌 How to Run
1. Clone the repo: `git clone https://github.com/solomonrd89/inventory-api.git`
2. Install dependencies: `pip install pymysql flask python-dotenv`
3. Setup Database: `python setup_db.py`
4. Run Server: `python app.py`
