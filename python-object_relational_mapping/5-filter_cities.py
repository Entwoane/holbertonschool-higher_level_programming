#!/usr/bin/python3
"""
Module to connect to a MySQL database and list all cities of a given state.

Usage:
    python3 script.py <mysql_username> <mysql_password>
    <database_name> <state_name>
"""
import MySQLdb
import sys


def main():
    """
    Main function to handle command line arguments and database operations.

    Retrieves cities from the database for a given state name
    ordered by ID, and prints them.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password>"
              "<database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        database=database_name,
    )
    cur = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    cities_name = [row[0] for row in rows]
    print(', '.join(cities_name))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
