#!/usr/bin/python3
import os
import sys

# Try MySQLdb first (common in ALX environments), then mysql-connector
DB_BACKEND = None
try:
    import MySQLdb  # type: ignore
    DB_BACKEND = "mysqldb"
except Exception:
    try:
        import mysql.connector  # type: ignore
        from mysql.connector import Error as MySQLError  # pylint: disable=import-error
        DB_BACKEND = "mysqlconnector"
    except Exception:
        DB_BACKEND = None


def get_credentials():
    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    # Support both MYSQL_PASSWORD and MYSQL_PWD
    pwd = os.getenv("MYSQL_PASSWORD", os.getenv("MYSQL_PWD", ""))
    return host, user, pwd


def main():
    if DB_BACKEND is None:
        print("Error: No MySQL Python driver found. Install either 'mysqlclient' (MySQLdb) or 'mysql-connector-python'.")
        sys.exit(1)

    host, user, pwd = get_credentials()

    conn = None
    cur = None
    try:
        if DB_BACKEND == "mysqldb":
            # Connect without specifying a database
            conn = MySQLdb.connect(host=host, user=user, passwd=pwd, port=3306)
            cur = conn.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            # MySQLdb autocommit may be off when no DB is selected; commit safely.
            conn.commit()

        elif DB_BACKEND == "mysqlconnector":
            conn = mysql.connector.connect(host=host, user=user, password=pwd)
            if not conn.is_connected():
                raise MySQLError("Connection reported not connected.")
            cur = conn.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            conn.commit()

        print("Database 'alx_book_store' created successfully!")

    except Exception as e:
        # Connection or execution failure
        print(f"Error: Could not connect to MySQL server or create database - {e}")
        sys.exit(1)

    finally:
        try:
            if cur is not None:
                cur.close()
        finally:
            if conn is not None:
                try:
                    # Some drivers require close even if not connected
                    conn.close()
                except Exception:
                    pass


if __name__ == "__main__":
    main()
