print("Script is starting...")
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

mydb = None
my_cursor = None

try:
    mydb = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

    my_cursor = mydb.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS products(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        price INT
    )
    """

    my_cursor.execute(query)
    mydb.commit()
    print("Success: Connected, Table Created, and Changes Saved!")

except Exception as err:
    print(f"Error: {err}")

finally:
    if my_cursor:
        my_cursor.close()
    if mydb:
        mydb.close()

    print("Connection Closed. Resources freed.")
