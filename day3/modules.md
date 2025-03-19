## 1. Investigate Circular Imports
### Problem:
Circular imports occur when two or more modules depend on each other. This can lead to import errors or unexpected behavior. Consider the following example:

#### module_a.py:
```python
import module_b

def func_a():
    return "Function A"

print(module_b.func_b())
```

#### module_b.py:
```python
import module_a

def func_b():
    return "Function B"
```

### Solution:
To fix this circular dependency, we can:
1. Use local imports inside functions instead of top-level imports.
2. Move common dependencies to a third module.
3. Use import statements inside function definitions to delay execution.

Example fix:
```python
# module_a.py

def func_a():
    return "Function A"

def call_func_b():
    from module_b import func_b  # Local import to avoid circular dependency
    print(func_b())
```

```python
# module_b.py

def func_b():
    return "Function B"
```

## 2. Dynamic Module Loading
### Task:
Write a program that dynamically imports and executes a function based on user input.

### Implementation:
```python
import importlib

module_name = input("Enter module name: ")
function_name = input("Enter function name: ")
argument = float(input("Enter argument: "))

module = importlib.import_module(module_name)
function = getattr(module, function_name)
print("Output:", function(argument))
```

## 3. Custom Module with Exception Handling
### Task:
Create a module `calculator.py` that handles division errors gracefully.

### Implementation:
```python
# calculator.py

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
```

```python
# main.py
import calculator

print(calculator.divide(10, 2))  # 5.0
print(calculator.divide(5, 0))   # Cannot divide by zero.
```

## 4. Advanced Import Strategies
### Task:
Write a script that imports a module, checks if a function exists, and executes it if available.

### Implementation:
```python
import importlib

def execute_function(module_name, function_name, *args):
    module = importlib.import_module(module_name)
    if hasattr(module, function_name):
        function = getattr(module, function_name)
        return function(*args)
    else:
        return "Function not found."

print(execute_function("math", "sqrt", 16))  # 4.0
```

## 5. Optimize Import Time
### Task:
Measure the import time for different methods.

### Implementation:
```python
import time
start = time.time()
import math
end = time.time()
print(f"Import time: {end - start}")
```

## 6. Module Creation and Distribution
### Task:
1. Create a package with `__init__.py`.
2. Write a `setup.py`.
3. Install and test the package locally.

### Implementation:

#### **Step 1: Write `my_module.py`**
Create `my_module.py` inside `my_package/`:

```python
def greet(name):
    return f"Hello, {name}!"
```

#### **Step 2: Write `__init__.py`**
Create `__init__.py` inside `my_package/`:

```python
from .my_module import greet
```

#### **Step 3: Write `setup.py`**
Create `setup.py` in the root directory:

```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Your Name",
    description="A sample package",
)
```

#### **Step 4: Install the Package Locally**
Run this command in the terminal:

```sh
pip install .
```

#### **Step 5: Test the Package**
Create a test script `test.py`:

```python
import my_package

print(my_package.greet("Alice"))  # Output: Hello, Alice!
```
## 7. Investigate sys.path
### Task:
Modify `sys.path` to include a custom directory.

### Implementation:
```python
import sys
from pathlib import Path

custom_path = Path("/custom/path/to/modules").resolve()
sys.path.append(str(custom_path))

try:
    import mymodule
    print("Module imported successfully.")
except ModuleNotFoundError:
    print("Module not found in the specified path.")
```

## 8. Mocking Modules for Testing
### Task:
Use `unittest.mock` to mock module functions during testing.

### Implementation:
```python
from unittest import mock
import math

def test_mock_sqrt():
    with mock.patch('math.sqrt', return_value=100):
        return math.sqrt(25)  # Should return 100

print(test_mock_sqrt())
```

## 9. Import Side Effects
### Task:
Create a module that runs code upon import.

### Implementation:
```python
# mymodule.py
print("Module has been imported successfully!")

def my_function():
    return "Hello from mymodule!"
```

## 10. Investigate Python’s Import Caching
### Task:
Explore `sys.modules` to understand how Python caches modules.

### Implementation:
```python
import sys
import mymodule

print("Cached module info:", sys.modules.get('mymodule'))

def reload_module():
    import importlib
    importlib.reload(mymodule)
    print("Module reloaded.")
```
