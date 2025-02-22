import mysql.connector

def get_sql_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="saimohan",
            database="grocery_store"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None  # Ensure it does not return None silently
