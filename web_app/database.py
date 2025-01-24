import sqlite3
from sqlite3 import Error

my_list = []
create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
      id INT PRIMARY KEY,
      description TEXT
      );
        """
select_tasks = "SELECT * FROM tasks"


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name, check_same_thread=False)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
