# Q1. Investigate Circular Imports
# module_a.py

def func_a():
    return "Function A"

def call_func_b():
    from module_b import func_b  # Local import to avoid circular dependency
    print(func_b())

# module_b.py

def func_b():
    return "Function B"

# Q2. Dynamic Module Loading
# dynamic_import.py

import importlib

module_name = input("Enter module name: ")
function_name = input("Enter function name: ")
argument = float(input("Enter argument: "))

module = importlib.import_module(module_name)
function = getattr(module, function_name)
print("Output:", function(argument))

# Q3. Importing Modules with Aliases
# calculator.py

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"

# main.py

import calculator

print(calculator.divide(10, 2))  # 5.0
print(calculator.divide(5, 0))   # Cannot divide by zero.

# Q4. Advanced Import Strategies
# advanced_import.py

def execute_function(module_name, function_name, *args):
    module = importlib.import_module(module_name)
    if hasattr(module, function_name):
        function = getattr(module, function_name)
        return function(*args)
    else:
        return "Function not found."

print(execute_function("math", "sqrt", 16))  # 4.0

# Q5. Optimize Import Time
# import_time.py


import time
start = time.time()
import math
end = time.time()
print(f"Import time: {end - start}")

# Q7. Importing Modules with Wildcards
# sys_path.py

import sys
from pathlib import Path

custom_path = Path("/custom/path/to/modules").resolve()
sys.path.append(str(custom_path))

try:
    import mymodule
    print("Module imported successfully.")
except ModuleNotFoundError:
    print("Module not found in the specified path.")

# Q8. Mocking Modules for Testing
# mock_test.py

from unittest import mock
import math

def test_mock_sqrt():
    with mock.patch('math.sqrt', return_value=100):
        return math.sqrt(25)  # Should return 100

print(test_mock_sqrt())

# Q9. Import Side Effects
# side_effect.py

print("Module has been imported successfully!")

def my_function():
    return "Hello from mymodule!"

# Q10. Investigate Python’s Import Caching
# import_cache.py

import sys
import mymodule

print("Cached module info:", sys.modules.get('mymodule'))

def reload_module():
    import importlib
    importlib.reload(mymodule)
    print("Module reloaded.")