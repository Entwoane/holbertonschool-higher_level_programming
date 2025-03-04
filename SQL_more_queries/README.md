# SQL - More queries

## General

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a **PRIMARY KEY**
- What’s a **FOREIGN KEY**
- How to use **NOT NULL** and **UNIQUE** constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are **JOIN** and **UNION**

## TASKS

0. My privileges!

Write a script that lists all privileges of the _MySQL_ users _user_0d_1_ and _user_0d_2_ on your server (in _localhost_).

File: 0-privileges.sql

1. Root user

Write a script that creates the MySQL server user _user_0d_1_.

- _user_0d_1_ should have all privileges on your MySQL server
- The _user_0d_1_ password should be set to _user_0d_1_pwd_
- If the user _user_0d_1_ already exists, your script should not fail

File: 1-create_user.sql

2. Read user

Write a script that creates the database _hbtn_0d_2_ and the user _user_0d_2_.

- _user_0d_2_ should have only **SELECT** privilege in the database _hbtn_0d_2_
- The _user_0d_2_ password should be set to _user_0d_2_pwd_
- If the database _hbtn_0d_2_ already exists, your script should not fail
- If the user _user_0d_2_ already exists, your script should not fail

3. Always a name

Write a script that creates the table _force_name_ on your MySQL server.

- _force_name_ description:
  - _id_ INT
  - _name_ VARCHAR(256) can’t be null
- The database name will be passed as an argument of the _mysql_ command
- If the table _force_name_ already exists, your script should not fail

File: 3-_force_name_.sql

4. ID can't be null

Write a script that creates the table _id_not_null_ on your MySQL server.

- _id_not_null_ description:
  - _id_ INT with the default value 1
  - _name_ VARCHAR(256)
- The database name will be passed as an argument of the _mysql_ command
- If the table _id_not_null_ already exists, your script should not fail

File: 4-never_empty.sql

5. Unique ID

Write a script that creates the table unique_id on your MySQL server.

- unique_id description:
  - _id_ INT with the default value 1 and must be unique
  - _name_ VARCHAR(256)
- The database name will be passed as an argument of the _mysql_ command
- If the table unique_id already exists, your script should not fail

File: 5-unique_id.sql

6. States table

Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

- states description:
  - _id_ INT unique, auto generated, can’t be null and is a primary key
  - _name_ VARCHAR(256) can’t be null
- If the database hbtn_0d_usa already exists, your script should not fail
- If the table states already exists, your script should not fail

File: 6-states.sql

7. Cities table

Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

- _cities_ description:
  - _id_ INT unique, auto generated, can’t be null and is a primary key
  - _state_id_ INT, can’t be null and must be a **FOREIGN KEY** that references to _id_ of the _states_ table
  - _name_ VARCHAR(256) can’t be null
- If the database _hbtn_0d_usa_ already exists, your script should not fail
- If the table _cities_ already exists, your script should not fail

File: 7-cities.sql

8. Cities of California

Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

- The states table contains only one record where _name_ = _California_ (but the id can be different, as per the example)
- Results must be sorted in ascending order by _cities.id_
- You are not allowed to use the **JOIN** keyword
- The database _name_ will be passed as an argument of the _mysql_ command

File: 8-cities_of_california_subquery.sql

9. Cities by States

Write a script that lists all cities contained in the database hbtn_0d_usa.

- Each record should display: _cities.id_ - _cities.name_ - _states.name_
- Results must be sorted in ascending order by _cities.id_
- You can use only one **SELECT** statement
- The database name will be passed as an argument of the _mysql_ command

File: 9-cities_by_state_join.sql

10. Genre ID by show

Import the database dump from _hbtn_0d_tvshows_ to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/*hbtn_0d_tvshows*.sql)

Write a script that lists all shows contained in _hbtn_0d_tvshows_ that have at least one genre linked.

- Each record should display: _tv_shows.title_ - _tv_show_genres.genre_id_
- Results must be sorted in ascending order by _tv_shows.title_ and _tv_show_genres.genre_id_
- You can use only one **SELECT** statement
- The database name will be passed as an argument of the _mysql_ command

File: 10-genre_id_by_show.sql

11. Genre ID for all shows
    mandatory

Import the database dump of _hbtn_0d_tvshows_ to your MySQL server: download (same as 10-genre_id_by_show.sql)

Write a script that lists all shows contained in the database _hbtn_0d_tvshows_.

- Each record should display: _tv_shows.title_ - _tv_show_genres.genre_id_
- Results must be sorted in ascending order by _tv_shows.title_ and _tv_show_genres.genre_id_
- If a show doesn’t have a genre, display **NULL**
- You can use only one **SELECT** statement
- The database name will be passed as an argument of the _mysql_ command

File: 11-genre_id_all_shows.sql

12. No genre

Import the database dump from _hbtn_0d_tvshows_ to your MySQL server (same as 11-genre_id_all_shows.sql)

Write a script that lists all shows contained in _hbtn_0d_tvshows_ without a genre linked.

- Each record should display: _tv_shows.title_ - _tv_show_genres.genre_id_
- Results must be sorted in ascending order by _tv_shows.title_ and _tv_show_genres.genre_id_
- You can use only one **SELECT** statement
- The database name will be passed as an argument of the _mysql_ command

File: 12-no_genre.sql

13. Number of shows by genre

Import the database dump from _hbtn_0d_tvshows_ to your MySQL server (same as 12-no_genre.sql)

Write a script that lists all genres from _hbtn_0d_tvshows_ and displays the number of shows linked to each.

- Each record should display: _\<TV Show genre>_ - _\<Number of shows linked to this genre>_
- First column must be called _genre_
- Second column must be called _number_of_shows_
- Don’t display a genre that doesn’t have any shows linked
- Results must be sorted in descending order by the number of shows linked
- You can use only one **SELECT** statement
- The database name will be passed as an argument of the _mysql_ command

File: 13-count_shows_by_genre.sql

14. My genres

Import the database dump from _hbtn_0d_tvshows_ to your MySQL server: (same as 13-count_shows_by_genre.sql)

Write a script that uses the _hbtn_0d_tvshows_ database to lists all genres of the show _Dexter_.

- The tv*shows table contains only one record where \_title* = _Dexter_ (but the _id_ can be different)
- Each record should display: _tv_genres.name_
- Results must be sorted in ascending order by the genre name
- You can use only one **SELECT** statement
- The database name will be passed as an argument of the _mysql_ command

File: 14-my_genres.sql

15. Only Comedy

Import the database dump from _hbtn_0d_tvshows_ to your MySQL server: (same as 14-my_genres.sql)

Write a script that lists all Comedy shows in the database _hbtn_0d_tvshows_.

- The tv*genres table contains only one record where \_name* = _Comedy_ (but the _id_ can be different)
- Each record should display: _tv_shows.title_
- Results must be sorted in ascending order by the show title
- You can use only one **SELECT** statement
- The database name will be passed as an argument of the _mysql_ command

File: 15-comedy_only.sql

16. List shows and genres

Import the database dump from _hbtn_0d_tvshows_ to your MySQL server: (same as 15-comedy_only.sql)

Write a script that lists all shows, and all genres linked to that show, from the database _hbtn_0d_tvshows_.

- If a show doesn’t have a genre, display **NULL** in the genre column
- Each record should display: _tv_shows.title_ - _tv_genres.name_
- Results must be sorted in ascending order by the show title and genre name
- You can use only one **SELECT** statement
- The database name will be passed as an argument of the _mysql_ command

File: 16-shows_by_genre.sql
