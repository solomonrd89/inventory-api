from flask import Flask, jsonify, request
import pymysql  # We use the library that worked for you
import pymysql.cursors  # Needed to make data look like JSON
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


# Helper function to get a database connection
def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        # This line is crucial for PyMySQL to return "Dictionaries" (JSON friendly)
        cursorclass=pymysql.cursors.DictCursor,
    )


# 1. The Home Page
@app.route("/")
def home():
    return "<h1>Inventory API is Running with PyMySQL!</h1>"


# 2. The "Add Product" Endpoint
# Usage: /add?name=Mouse&price=500
@app.route("/add", methods=["GET"])
def add_product():
    name = request.args.get("name")
    price = request.args.get("price")

    if not name or not price:
        return "Error: Please provide name and price (e.g., /add?name=Mouse&price=500)"

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # The SQL Query to insert data
        query = "INSERT INTO products (name, price) VALUES (%s, %s)"
        cursor.execute(query, (name, price))

        conn.commit()
        cursor.close()
        conn.close()

        return f"Success! Added {name} for {price} rupees."

    except Exception as e:
        return f"Error: {e}"


# 3. The "View Products" Endpoint
# This fetches data FROM the database
@app.route("/products")
def get_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()  # This gets the list of items

        cursor.close()
        conn.close()

        return jsonify(products)  # Turns the Python list into Web JSON

    except Exception as e:
        return f"Error: {e}"


# 4. The "Search" Endpoint
# Usage: /search?q=phone
@app.route("/search")
def search_product():
    query_term = request.args.get("q")  # Get the search word (e.g., "phone")

    if not query_term:
        return "Error: Please provide a search term (e.g., /search?q=laptop)"

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # The SQL Logic:
        # LIKE %...% means "contains this word anywhere"
        # If I search "phone", it finds "iPhone", "Headphones", "Telephone"
        sql_query = "SELECT * FROM products WHERE name LIKE %s"

        # We add the % symbols around the word for the SQL syntax
        search_pattern = f"%{query_term}%"

        cursor.execute(sql_query, (search_pattern,))
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        if not results:
            return "No products found matching that name."

        return jsonify(results)

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
