# Python - Data Structures: Lists, Tuples

Learning what are lists and how to use them, differences between lists and strings, what are tuples and how to use them and the usages of tuples versus lists. What is sequence unpacking. What is the **del()** statement and how to use it

## TASKS

### 0. Print a list of integers

Write a function that prints all integers of a list.

- Prototype: **def print_list_integer(my_list=[]):**
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use **str.format()** to print integers

File: [0-print_list_integer.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/0-print_list_integer.py)

### 1. Secure access to an element in a list

Write a function that retrieves an element from a list.

- Prototype: **def element_at(my_list, idx):**
- If _idx_ is negative, the function should return **None**
- If _idx_ is out of range (> of number of element in _my_list_), the function should return **None**
- You are not allowed to import any module
- You are not allowed to use **try/except**

File: [1-element_at.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/1-element_at.py)

### 2. Replace element

Write a function that replaces an element of a list at a specific position.

- Prototype: **def replace_in_list(my_list, idx, element):**
- If _idx_ is negative, the function should not modify anything, and returns the original list
- If _idx_ is out of range (> of number of element in **my_list**), the function should not modify anything, and- returns the original list
- You are not allowed to import any module
- You are not allowed to use **try/except**

File: [2-replace_in_list.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/2-replace_in_list.py)

### 3. Print a list of integers... in reverse

Write a function that prints all integers of a list, in reverse order.

- Prototype: **def print_reversed_list_integer(my_list=[]):**
- Format: one integer per line.
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use **str.format()** to print integers

File: [3-print_reversed_list_integer.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/3-print_reversed_list_integer.py)

### 4. Replace in a copy

Write a function that replaces an element in a list at a specific position without modifying the original list.

- Prototype: **def new_in_list(my_list, idx, element):**
- If _idx_ is negative, the function should return a copy of the original _list_
- If _idx_ is out of range (> of number of element in **my_list**), the function should return a copy of the original- list
- You are not allowed to import any module
- You are not allowed to use **try/except**

File: [4-new_in_list.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/4-new_in_list.py)

### 5. Can you C me now?

Write a function that removes all characters _c_ and _C_ from a string.

- Prototype: **def no_c(my_string):**
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use **str.replace()**

File: [5-no_c.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/5-no_c.py)

### 6. Lists of lists = Matrix

Write a function that prints a matrix of integers.

- Prototype: **def print_matrix_integer(matrix=[[]]):**
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use **str.format()** to print integers

File: [6-print_matrix_integer.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/6-print_matrix_integer.py)

### 7. Tuples addition

Write a function that adds 2 tuples.

- Prototype: **def add_tuple(tuple_a=(), tuple_b=()):**
- Returns a tuple with 2 integers:
  - The first element should be the addition of the first element of each argument
  - The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value _0_ for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers

File: [7-add_tuple.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/7-add_tuple.py)

### 8. More returns

Write a function that returns a tuple with the length of a string and its first character.

- Prototype: **def multiple_returns(sentence):**
- If the sentence is empty, the first character should be equal to **None**
- You are not allowed to import any module

File: [8-multiple_returns.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/8-multiple_returns.py)

### 9. Find the max

Write a function that finds the biggest integer of a list.

- Prototype: **def max_integer(my_list=[]):**
- If the list is empty, return **None**
- You can assume that the list only contains integers
- You are not allowed to import any module
- You are not allowed to use the builtin **max()**

File: [9-max_integer.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/9-max_integer.py)

### 10. Only by 2

Write a function that finds all multiples of 2 in a list.

- Prototype: **def divisible_by_2(my_list=[]):**
- Return a new list with **True** or **False**, depending on whether the integer at the same position in the original- list is a multiple of 2
- The new list should have the same size as the original list
- You are not allowed to import any module

File: [10-divisible_by_2.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/10-divisible_by_2.py)

### 11. Delete at

Write a function that deletes the item at a specific position in a list.

- Prototype: **def delete_at(my_list=[], idx=0):**
- If _idx_ is negative or out of range, nothing change (returns the same list)
- You are not allowed to use _pop()_
- You are not allowed to import any module

File: [11-delete_at.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/11-delete_at.py)

### 12. Switch

Complete the [source code](https://github.com/hs-hq/0x03.py/blob/main/12-switch_py) in order to switch value of **a** and **b**

- Your code should be inserted where the comment is (line 4)
- Your program should be exactly 5 lines long

File: [12-switch.py](https://github.com/Entwoane/holbertonschool-higher_level_programming/blob/main/python-data_structures/12-switch.py)
