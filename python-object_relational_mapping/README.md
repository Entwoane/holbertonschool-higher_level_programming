# Python - Object-relational mapping

## General

- How to connect to a MySQL database from a Python script
- How to **SELECT** rows in a MySQL table from a Python script
- How to **INSERT** rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## TASKS

0. Get all states

Write a script that lists all states from the database hbtn_0e_0_usa:

- Your script should take 3 arguments: _mysql username_, mysql password and database name (no argument validation needed)
- You must use the module _MySQLdb_ (_import MySQLdb_)
- Your script should connect to a MySQL server running on _localhost_ at port _3306_
- Results must be sorted in ascending order by _states.id_
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: 0-select_states.py

1. Filter states

Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

- Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: 1-filter_states.py

2. Filter states by user input

Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

- Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- You must use format to create the SQL query with the user input
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: 2-my_filter_states.py

3.  SQL Injection...
    Wait, do you remember the previous task? Did you test **_"Arizona'; TRUNCATE TABLE states ; SELECT \* FROM states WHERE name = '"_** as an input?

        guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
        (2, 'Arizona')
        guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
        guillaume@ubuntu:~/$

What? Empty?

Yes, it’s an [SQL injection](https://intranet.hbtn.io/rltoken/d0bQ5pmhaRPHtf0OJI9-Vg) to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

- Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: 3-my_safe_filter_states.py

4. Cities by states

Write a script that lists all cities from the database hbtn_0e_4_usa

- Your script should take 3 arguments: mysql username, mysql password and database name
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: 4-cities_by_state.py

5. All cities by state

Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

- Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

File: 5-filter_cities.py

6. First state model

Write a python file that contains the class definition of a State and an instance Base = declarative_base():

- State class:
  - inherits from Base Tips
  - links to the MySQL table states
  - class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  - class attribute name that represents a column of a string with maximum 128 characters and can’t be null
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server running on localhost at port 3306
- WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)

File: model_state.py

7. All states via SQLAlchemy

Write a script that lists all State objects from the database hbtn_0e_6_usa

- Your script should take 3 arguments: mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

File: 7-model_state_fetch_all.py

8. First state

Write a script that prints the first State object from the database hbtn_0e_6_usa

- Your script should take 3 arguments: mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at port 3306
- The state you display must be the first in states.id
- You are not allowed to fetch all states from the database before displaying the result
- The results must be displayed as they are in the example below
- If the table states is empty, print Nothing followed by a new line
- Your code should not be executed when imported

File: 8-model_state_fetch_first.py

9. Contains \`a`

Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

- Your script should take 3 arguments: mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

File: 9-model_state_filter_a.py

10. Get a state

Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa

- Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at port 3306
- You can assume you have one record with the state name to search
- Results must display the states.id
- If no state has the name you searched for, display Not found
- Your code should not be executed when imported

File: 10-model_state_my_get.py

11. Add a new state

Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

- Your script should take 3 arguments: mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at port 3306
- Print the new states.id after creation
- Your code should not be executed when imported

File: 11-model_state_insert.py

12. Update a state

Write a script that changes the name of a State object from the database hbtn_0e_6_usa

- Your script should take 3 arguments: mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at port 3306
- Change the name of the State where id = 2 to New Mexico
- Your code should not be executed when imported

File: 12-model_state_update_id_2.py

13. Delete states

Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

- Your script should take 3 arguments: mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at port 3306
- Your code should not be executed when imported

File: 13-model_state_delete_a.py

14. Cities in state

Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

- City class:
  - inherits from Base (imported from model_state)
  - links to the MySQL table cities
  - class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  - class attribute name that represents a column of a string of 128 characters and can’t be null
  - class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
- You must use the module SQLAlchemy

Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:

- Your script should take 3 arguments: mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import Base, State
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- Results must be display as they are in the example below (\<state name>: (\<city id>) \<city name>)
- Your code should not be executed when imported

Files: model_city.py, 14-model_city_fetch_by_state.py
