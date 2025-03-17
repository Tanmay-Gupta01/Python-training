

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




# 2.6. Type Conversion Functions
# 2. **Exercise:**
#    - Convert variables between types and observe the results:
#      ```python
#      num = '123'
#      converted_num = int(num)
#      print(converted_num, type(converted_num))
#      ```


binary_str = "1101"
binary_num = int(binary_str, 2)  # Convert binary string to an integer
print(binary_num, type(binary_num))

decimal_val = 99.99
int_val = int(decimal_val)  # Convert float to int (truncation)
print(int_val, type(int_val))

bool_val = bool(0)  # Convert an integer to boolean
print(bool_val, type(bool_val))


# 2.7. Variables2. **Exercise:**
#    - Assign values to variables, print them, and observe changes upon reassignment.

message = "Hello, Python!"
print("Original Message:", message)
message = "Welcome to coding!"
print("Updated Message:", message)


# 2.8. Variable Names and Keywords

# 1. **Exercise:**
#    - Try using reserved keywords as variable names and observe the errors.
import keyword
print("Python Reserved Keywords:", keyword.kwlist)

# Trying to use a reserved keyword as a variable (will cause an error)
# class = "Programming"  # Uncommenting this will cause an error


# 2.9. Choosing the Right Variable Name
# Poor variable naming
a = 1000
b = 0.15
c = a - (a * b)
print("Poor Naming Result:", c)

# Better variable naming
original_price = 1000
discount_percentage = 0.15
final_price = original_price - (original_price * discount_percentage)
print("Better Naming Result:", final_price)


# 2.10. Statements and Expressions
result = (10 + 5) * 3  # This is an expression
print(result)  # This is a statement


# 2.11. Order of Operations
calculation = 10 + 3 * 5 ** 2 // 2 - 4
print("Order of Operations Result:", calculation)


# 2.12. Reassignment
counter = 1
print("Initial Counter:", counter)
counter = counter + 4
print("Updated Counter:", counter)


# 2.13. Updating Variables
balance = 5000
balance += 2000  # Add money
print("Updated Balance:", balance)

balance -= 500  # Deduct money
print("Final Balance:", balance)
