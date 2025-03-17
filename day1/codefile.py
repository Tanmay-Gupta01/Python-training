

# 2.2. Values and Data Types
# 3. **Exercise:**
#    - Write a program that:
#      - Assigns different values to variables.
#      - Prints the type of each variable.

# Assigning different values to variables
x = 42        # Integer
y = 3.14      # Float
z = "Hello"   # String
a = True      # Boolean
b = [1, 2, 3] # List
c = (4, 5, 6) # Tuple
d = {7, 8, 9} # Set
e = {"key": "value"} # Dictionary
f = None      # NoneType

# Printing the type of each variable
print(type(x), type(y), type(z))
print(type(a), type(b), type(c))
print(type(d), type(e), type(f))






# 2.3. Operators and Operands
# 3. **Exercise:**
#    - Create a Python script that demonstrates:
#      - Addition, subtraction, multiplication, and division.
#      - Comparisons between numbers.
#      - Logical operations like `and`, `or`, `not`.

# Arithmetic Operations
a = 10
b = 5

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Comparison Operations
print("a is equal to b:", a == b)
print("a is not equal to b:", a != b)
print("a is greater than b:", a > b)
print("a is less than b:", a < b)
print("a is greater than or equal to b:", a >= b)
print("a is less than or equal to b:", a <= b)

# Logical Operations
x = True
y = False

print("x AND y:", x and y)
print("x OR y:", x or y)
print("NOT x:", not x)


## 2.4. Function Calls

### 2.4.1. Function Calls as Part of Complex Expressions

# 1. **Fun Fact:**
#    - In Python, functions are first-class objects, meaning they can be assigned to variables and passed as arguments.
# 2. **Exercise:**
#    - Write a program that uses built-in functions inside expressions:
#      ```python
#      numbers = [5, 3, 8, 1]
#      print(max(numbers) - min(numbers))
#      ```


# Using built-in functions inside expressions

numbers = [5, 3, 8, 1]

# Calculating the difference between the maximum and minimum values
difference = max(numbers) - min(numbers)

print("Difference between max and min:", difference)




### 2.4.2. Functions are Objects; Parentheses Invoke Functions

# 1. **Exercise:**
#    - Assign a function to a variable, then call the function using the new variable:
#      ```python
#      greet = print
#      greet('Hello, World!')
#      ```

# Assigning a function to a variable and calling it

def square(num):
    return num * num

calculate = square  # Assigning function to a variable

result = calculate(5)  # Calling the function using the new variable
print("Square of 5:", result)



## 2.5. Data Types
# 2. **Exercise:**
#    - Create variables of different types and print their types:
#      ```python
#      a = 10
#      b = 'Python'
#      c = 3.14
#      print(type(a), type(b), type(c))
#      ```

# Creating variables of different data types
a = 10          # Integer
b = "Python"    # String
c = 3.14        # Float
d = True        # Boolean
e = [1, 2, 3]   # List
f = (4, 5, 6)   # Tuple
g = {7, 8, 9}   # Set
h = {"name": "Alice", "age": 25}  # Dictionary
i = None        # NoneType

# Printing the type of each variable
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i))

