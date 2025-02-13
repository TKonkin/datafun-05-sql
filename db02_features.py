import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def update_records():
    """Function to read and execute SQL statements to update records"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_features", "update_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records updated successfully.")
    except sqlite3.Error as e:
        print("Error updating records:", e)

def delete_records():
    """Function to read and execute SQL statements to delete records"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_features", "delete_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting records:", e)

def main():
    update_records()
    delete_records()

if __name__ == "__main__":
    main()