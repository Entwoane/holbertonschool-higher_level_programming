#!/usr/bin/python3
"""
Module to connect to a MySQL database and list all State objects.

Usage:
    python3 script.py <mysql_username> <mysql_password> <mysql_database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Main function to handle command line arguments and database operations.

    Retrieves all State objects from the database,
    ordered by ID, and prints them.
    """
    # Verification of all required arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <mysql_database>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connection to SQLAlchemy engine
        engine = create_engine(
            'mysql+pymysql://{}:{}@localhost:3306/{}'
            .format(username, password, database),
            pool_pre_ping=True
        )

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retrieve all State objects, ordered by ID
        states = session.query(State).order_by(State.id.asc()).all()

        # Print each State object
        for state in states:
            print(f"{state.id}: {state.name}")

        # Close the session
        session.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
