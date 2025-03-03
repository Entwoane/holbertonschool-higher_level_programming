# SQL - Introduction

## General

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does _DDL_ and _DML_ stand for
- How to _CREATE_ or _ALTER_ a table
- How to _SELECT_ data from a table
- How to _INSERT_, _UPDATE_ or _DELETE_ data
- What are _subqueries_
- How to use MySQL functions

### _Working on Holberton School's Sandbox_

## TASKS

0. List databases

Write a script that lists all databases of your MySQL server.

File: 0-list_databases.sql

1. Create a database

Write a script that creates the database _hbtn_0c_0_ in your MySQL server.

- If the database _hbtn_0c_0_ already exists, your script should not fail
- You are not allowed to use the **SELECT** or **SHOW** statements

File: 1-create_database_if_missing.sql

2. Delete a database

Write a script that deletes the database _hbtn_0c_0_ in your MySQL server.

- If the database _hbtn_0c_0_ doesn’t exist, your script should not fail
- You are not allowed to use the **SELECT** or **SHOW** statements

File: 2-remove_database.sql

3. List tables

Write a script that lists all the tables of a database in your MySQL server.

- The database name will be passed as argument of _mysql_ command (in the following example: _mysql_ is the name of the database)

File: 3-list_tables.sql

4. First table

Write a script that creates a table called _first_table_ in the current database in your MySQL server.

- _first_table_ description:
  - _id_ INT
  - _name_ VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table _first_table_ already exists, your script should not fail
- You are not allowed to use the **SELECT** or **SHOW** statements

File: 4-first_table.sql

5. Full description

Write a script that prints the following description of the table _first_table_ from the database _hbtn_0c_0_ in your MySQL server.

- The database name will be passed as an argument of the _mysql_ command
- You are not allowed to use the **DESCRIBE** or **EXPLAIN** statements

File: 5-full_table.sql

6. List all in table

Write a script that lists all rows of the table _first_table_ from the database _hbtn_0c_0_ in your MySQL server.

- All fields should be printed
- The database name will be passed as an argument of the _mysql_ command

File: 6-list_values.sql

7. First add

Write a script that inserts a new row in the table _first_table_ (database _hbtn_0c_0_) in your MySQL server.

- New row:
  - _id_ = **89**
  - _name_ = **Best** **School**
- The database name will be passed as an argument of the _mysql_ command

File: 7-insert_value.sql

8. Count 89

Write a script that displays the number of records with _id = 89_ in the table _first_table_ of the database _hbtn_0c_0_ in your MySQL server.

- The database name will be passed as an argument of the _mysql_ command

File: 8-count_89.sql

9. Full creation

Write a script that creates a table _second_table_ in the database _hbtn_0c_0_ in your MySQL server and add multiples rows.

- _second_table_ description:
  - **id** INT
  - **name** VARCHAR(256)
  - **score** INT
- The database name will be passed as an argument to the _mysql_ command
- If the table _second_table_ already exists, your script should not fail
- You are not allowed to use the SELECT and SHOW statements
- Your script should create these records:
  - **id** = 1, **name** = “John”, **score** = 10
  - **id** = 2, **name** = “Alex”, **score** = 3
  - **id** = 3, **name** = “Bob”, **score** = 14
  - **id** = 4, **name** = “George”, **score** = 8

File: 9-full_creation.sql

10. List by best

Write a script that lists all records of the table _second_table_ of the database _hbtn_0c_0_ in your MySQL server.

- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the _mysql_ command

File: 10-top_score.sql

11. Select the best

Write a script that lists all records with a _score >= 10_ in the table _second_table_ of the database _hbtn_0c_0_ in your MySQL server.

- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the _mysql_ command

File: 11-best_score.sql

12. Cheating is bad

Write a script that updates the score of Bob to _10_ in the table _second_table_.

- You are not allowed to use Bob’s id value, only the _name_ field
- The database name will be passed as an argument of the _mysql_ command

File: 12-no_cheating.sql

13. Score too low

Write a script that removes all records with a _score <= 5_ in the table _second_table_ of the database _hbtn_0c_0_ in your MySQL server.

- The database name will be passed as an argument of the _mysql_ command

File: 13-change_class.sql

14. Average

Write a script that computes the score average of all records in the table _second_table_ of the database _hbtn_0c_0_ in your MySQL server.

- The result column name should be _average_
- The database name will be passed as an argument of the _mysql_ command

File: 14-average.sql

15. Number by score

Write a script that lists the number of records with the same score in the table _second_table_ of the database _hbtn_0c_0_ in your MySQL server.

- The result should display:
  - the _score_
  - the number of records for this _score_ with the label _number_
- The list should be sorted by the number of records (descending)
- The database name will be passed as an argument to the _mysql_ command

File: 15-groups.sql

16. Say my name

Write a script that lists all records of the table _second_table_ of the database _hbtn_0c_0_ in your MySQL server.

- Don’t list rows without a _name_ value
- Results should display the score and the name (in this order)
- Records should be listed by descending score
- The database name will be passed as an argument to the _mysql_ command

File: 16-no_link.sql
