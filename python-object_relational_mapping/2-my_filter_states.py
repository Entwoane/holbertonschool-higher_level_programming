#!/usr/bin/python3
"""
Module to connect to a MySQL database and retrieve states by name
ordered by ID.

Usage:
    python3 script.py <mysql_username> <mysql_password>
    <database_name> <state_name>
"""
import MySQLdb
import sys


def main():
    """
    Main function to handle command line arguments and database operations.

    Retrieves states from the database where the name matches
    the given state name, ordered by ID, and prints them.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        database=database_name
    )

    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}'"
             "ORDER BY id ASC".format(state_name_searched))
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(f"({row[0]}, '{row[1]}')")

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
