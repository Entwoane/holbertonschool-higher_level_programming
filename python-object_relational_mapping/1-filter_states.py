#!/usr/bin/python3
"""
Module to connect to a MySQL database and retrieve states starting with 'N'
ordered by ID.

Usage:
    python3 script.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys


def main():
    """
    Main function to handle command line arguments and database operations.

    Retrieves states from the database where the name starts with 'N'
    ordered by ID, and prints them.
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
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
