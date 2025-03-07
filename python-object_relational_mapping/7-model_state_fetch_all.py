#!/usr/bin/python3
"""
Module to connect to a MySQL database and list all states ordered by ID.

Usage:
    python3 script.py <mysql_username> <mysql_password> <mysql_database>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """
    Main function to handle command line arguments and database operations.

    Retrieves all states from the database, ordered by ID, and prints them.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <mysql database>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
