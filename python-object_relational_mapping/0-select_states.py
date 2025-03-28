#!/usr/bin/python3
"""
Module to connect to a MySQL database and retrieve all states ordered by ID.

Usage:
    python3 script.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys


def main():
    """
    Main function to handle command line arguments and database operations.

    Retrieves all states from the database and prints them.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        database=database_name
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(f"({row[0]}, '{row[1]}')")

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
