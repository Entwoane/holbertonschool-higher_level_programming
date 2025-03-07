#!/usr/bin/python3
"""
Module to connect to a MySQL database and list all cities ordered by ID.

Usage:
    python3 script.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys


def main():
    """
    Main function to handle command line arguments and database operations.

    Retrieves all cities from the database, ordered by ID, and prints them.
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
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
