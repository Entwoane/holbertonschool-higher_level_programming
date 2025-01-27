# Python - Classes and Objects

## General

- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special \_\_init\_\_ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the \_\_dict\_\_ of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

## TASKS

### 0. My first square

Write an empty class **Square** that defines a square:

- You are not allowed to import any module

File:0-square.py

### 1. Square with size

Write a class **Square** that defines a square by: (based on 0-square.py)

- Private instance attribute: **_size_**
- Instantiation with **_size_** (no type/value verification)
- You are not allowed to import any module

**Why?**
_Why ***size*** is private attribute?_

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

File: 1-square.py

### 2. Size validation

Write a class **Square** that defines a square by: (based on 1-square.py)

- Private instance attribute: **_size_**
- Instantiation with optional size: **_def \_\_init\_\_(self, size=0):_**
  - **_size_** must be an integer, otherwise raise a **_TypeError_** exception with the message _size must be an integer_
  - if **_size_** is less than **_0_**, raise a **_ValueError_** exception with the message _size must be >= 0_
- You are not allowed to import any module

File: 2-square.py

### 3. Area of a square

Write a class **Square** that defines a square by: (based on 2-square.py)

- Private instance attribute: **_size_**
- Instantiation with optional size: **_def \_\_init\_\_(self, size=0):_**
  - **_size_** must be an integer, otherwise raise a **_TypeError_** exception with the message _size must be an integer_
  - if **_size_** is less than **_0_**, raise a **_ValueError_** exception with the message _size must be >= 0_
- Public instance method: **_def area(self):_** that returns the current square area
- You are not allowed to import any module

File: 3-square.py

### 4. Access and update private attribute

Write a class **Square** that defines a square by: (based on 3-square.py)

- Private instance attribute: _size_:
  - property **_def size(self):_** to retrieve it
  - property setter **_def size(self, value):_** to set it:
    - **_size_** must be an integer, otherwise raise a **_TypeError_** exception with the message _size must be an integer_
    - if **_size_** is less than 0, raise a **_ValueError_** exception with the message _size must be >= 0_
- Instantiation with optional size: **_def \_\_init\_\_(self, size=0):_**
- Public instance method: **_def area(self):_** that returns the current square area
- You are not allowed to import any module

**Why?**
_Why a getter and setter?_

Reminder: _size_ is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

File: 4-square.py

### 5. Printing a square

Write a class **Square** that defines a square by: (based on 4-square.py)

- Private instance attribute: _size_:
  - property **def size(self):** to retrieve it
  - property setter **def size(self, value):** to set it:
    - **_size_** must be an integer, otherwise raise a **_TypeError_** exception with the message _size must be an integer_
    - if **_size_** is less than **_0_**, raise a **_ValueError_** exception with the message _size must be >= 0_
- Instantiation with optional size: **def \_\_init\_\_(self, size=0):**
- Public instance method: **def area(self):** that returns the current square area
- Public instance method: **def my_print(self):** that prints in stdout the square with the character #:
  - if **_size_** is equal to 0, print an empty line
- You are not allowed to import any module

File: 5-square.py

### 6. Coordinates of a square

Write a class **Square** that defines a square by: (based on 5-square.py)

- Private instance attribute: _size_:
  - property **def size(self):** to retrieve it
  - property setter **def size(self, value):** to set it:
    - **_size_** must be an integer, otherwise raise a **_TypeError_** exception with the message _size must be an integer_
    - if **_size_** is less than **_0_**, raise a **_ValueError_** exception with the message _size must be >= 0_
- Private instance attribute: _position_:
  - property **def position(self):** to retrieve it
  - property setter **def position(self, value):** to set it:
    - _position_ must be a tuple of 2 positive integers, otherwise raise a **_TypeError_** exception with the message _position must be a tuple of 2 positive integers_
- Instantiation with optional **_size_** and optional position: **def \_\_init\_\_(self, size=0, position=(0, 0)):**
- Public instance method: **def area(self):** that returns the current square area
- Public instance method: **def my_print(self):** that prints in stdout the square with the character #:
  - if **_size_** is equal to 0, print an empty line
  - **_position_** should be use by using space - **Don’t fill lines by spaces** when **_position[1] > 0_**
- You are not allowed to import any module

File: 6-square.py
