import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_create", "02_create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)       
        
def insert_records():
    """Function to read and execute SQL statements to insert records into tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_create", "03_insert_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting records:", e) 
        
def main():
    create_database()
    create_tables()
    insert_records()

if __name__ == "__main__":
    main()