## 2.2. Values and Data Types

1.  What is a value in Python?
    - In Python, a value is any piece of data that a program manipulates. It can be a number, text, or more complex data like lists or dictionaries. Every value belongs to a specific data type.

2. Identify different data types in Python (e.g., integers, floats, strings, booleans).

##### 1. Numeric Types
Python supports different types of numbers:

- **Integer (`int`)**: Whole numbers without a decimal point.  
  - Example: `-10, 0, 25, 1000`
- **Floating-point (`float`)**: Numbers with decimal points.  
  - Example: `3.14, -2.5, 0.0`
- **Complex (`complex`)**: Numbers with real and imaginary parts.  
  - Example: `2 + 3j, -1.5 + 4.2j`

##### 2. Text Type
- **String (`str`)**: A sequence of characters enclosed in quotes.
  - Example: `"Hello, Python!"`, `'Data Science'`

##### 3. Boolean Type
- **Boolean (`bool`)**: Represents logical values `True` or `False`.
  - Example: `is_valid = True`

##### 4. Sequence Types
- **List (`list`)**: Ordered, mutable collection of elements.
  - Example: `[1, 2, 3, "Python", True]`
- **Tuple (`tuple`)**: Ordered, immutable collection of elements.
  - Example: `(10, 20, 30, "Data")`
- **Range (`range`)**: Generates a sequence of numbers.
  - Example: `range(1, 10)  # 1 to 9`

##### 5. Set Types
- **Set (`set`)**: Unordered, mutable collection of unique values.
  - Example: `{1, 2, 3, 4}`
- **Frozen set (`frozenset`)**: Immutable version of a set.
  - Example: `frozenset({10, 20, 30})`

##### 6. Mapping Type
- **Dictionary (`dict`)**: Collection of key-value pairs.
  - Example: `{ "name": "Alice", "age": 25, "city": "London" }`

##### 7. Special Type
- **NoneType (`None`)**: Represents the absence of a value.
  - Example: `value = None`

##### 8. Type Checking and Conversion
- Check the type of a variable:  
  ```python
  print(type(10))  # Output: <class 'int'>
  ```

---

## 2.3. Operators and Operands
1. **Research:**
   #### Learn about arithmetic, comparison, and logical operators.
---  

##### 1. Arithmetic Operators
These operators perform mathematical operations on numeric values. The basic arithmetic operations include:
- **Addition (`+`)**: Combines two values to produce their sum.
- **Subtraction (`-`)**: Computes the difference between two numbers.
- **Multiplication (`*`)**: Multiplies two numbers to give their product.
- **Division (`/`)**: Divides one number by another, resulting in a floating-point value.
- **Floor Division (`//`)**: Similar to division but rounds down the result to the nearest integer.
- **Modulus (`%`)**: Returns the remainder of a division operation.
- **Exponentiation (`**`)**: Raises a number to the power of another.

##### 2. Comparison Operators
These operators compare two values and return a Boolean result (`True` or `False`). They help in making decisions in conditional statements.
- **Equal to (`==`)**: Checks if two values are the same.
- **Not equal to (`!=`)**: Verifies if two values are different.
- **Greater than (`>`)**: Checks if the left operand is greater than the right operand.
- **Less than (`<`)**: Determines if the left operand is smaller than the right operand.
- **Greater than or equal to (`>=`)**: Ensures the left operand is either greater than or equal to the right operand.
- **Less than or equal to (`<=`)**: Ensures the left operand is either less than or equal to the right operand.

##### 3. Logical Operators
Logical operators are used to form compound conditions by combining multiple comparison statements.
- **AND (`and`)**: Returns `True` if both conditions are true; otherwise, it returns `False`.
- **OR (`or`)**: Returns `True` if at least one of the conditions is true.
- **NOT (`not`)**: Negates the result, turning `True` into `False` and vice versa.

---

