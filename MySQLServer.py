#!/usr/bin/python3
"""
MySQLServer.py
Script to create a database 'alx_book_store' in MySQL server.
If the database already exists, it will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (adjust user & password accordingly)
        connection = mysql.connector.connect(
            host="localhost",
            user="Antwiwaa",        
            password="ant12" 
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Safely close connection
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed.")  # Optional logging

if __name__ == "__main__":
    create_database()
