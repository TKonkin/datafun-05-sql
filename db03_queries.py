import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def perform_aggs():
    """Function to read and execute SQL statements to perform aggregations"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_queries", "query_aggregation.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)

            cursor = conn.cursor()
            sql_statements = [
               "SELECT AVG(year_published) FROM books", 
               "SELECT SUM(year_born) FROM authors"
            ]

            for statement in sql_statements:
                cursor.execute(statement)
            
            
            results = cursor.fetchall()
            for row in results:
                print(row)   
            
    except sqlite3.Error as e:
        print("Error aggregating records:", e)



def main():
    perform_aggs()
    

if __name__ == "__main__":
    main()