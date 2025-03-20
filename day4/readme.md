# Assignment Solution

## 1. Define a sequence. What types of sequences exist in Python?
A sequence is an ordered collection of items. Python has several sequence types:

- **Strings (`str`)**: Immutable, stores characters.
- **Lists (`list`)**: Mutable, stores elements of different types.
- **Tuples (`tuple`)**: Immutable, similar to lists but cannot be modified.
- **Ranges (`range`)**: Immutable sequence of numbers.
- **Byte sequences (`bytes`, `bytearray`)**: Stores binary data.

## 2. How are strings, lists, and tuples different from each other?
- **Strings (`str`)**: Immutable and stores a sequence of characters.
- **Lists (`list`)**: Mutable and can store multiple data types.
- **Tuples (`tuple`)**: Immutable like strings but can hold multiple data types like lists.

## 3. Explain how indexing works in Python with an example.
Indexing starts from `0` for positive values and `-1` for negative values.
```python
string = "Python"
print(string[0])   # Output: P
print(string[-1])  # Output: n
```

## 4. Write code to access the last character of a string.
```python
s = "Hello"
print(s[-1])  # Output: o
```

## 5. Create a list of numbers and access the third element.
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[2])  # Output: 30
```

## 6. What is the result of `len([1, [2, 3], 4])` and why?
**Output:** `3` because the list contains three elements: `1`, `[2,3]`, and `4`.

## 7. Explain slicing with a practical example.
```python
s = "Python Programming"
print(s[0:6])  # Output: Python
```

## 8. How would you reverse a string using slicing?
```python
s = "Python"
print(s[::-1])  # Output: nohtyP
```

## 9. Demonstrate list concatenation and repetition with examples.
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Concatenation Output: [1, 2, 3, 4, 5, 6]
print(list1 * 2)      # Repetition Output: [1, 2, 3, 1, 2, 3]
```

## 10. Write code to count the occurrences of an element in a list.
```python
lst = [1, 2, 2, 3, 4, 2]
print(lst.count(2))  # Output: 3
```

## 11. What will `my_tuple = (1, 2, 3); print(my_tuple[1:])` output?
**Output:** `(2, 3)`

## 12. Explain the difference between `list.append()` and `list.extend()`.
- `append(x)`: Adds `x` as a single element.
- `extend(iterable)`: Adds elements of `iterable` individually.

```python
lst = [1, 2]
lst.append([3, 4])  # Output: [1, 2, [3, 4]]
lst = [1, 2]
lst.extend([3, 4])  # Output: [1, 2, 3, 4]
```

## 13. Write code to split the sentence: "Learn Python, step by step!" into words.
```python
sentence = "Learn Python, step by step!"
print(sentence.split())  # Output: ['Learn', 'Python,', 'step', 'by', 'step!']
```

## 14. Join a list `['Python', 'is', 'fun']` into a single string.
```python
words = ['Python', 'is', 'fun']
print(" ".join(words))  # Output: "Python is fun"
```

## 15. Given a list `numbers = [1, 2, 2, 3, 4, 2]`, find the index of the first `2`.
```python
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.index(2))  # Output: 1
```

## 16. Write code to check if a string is a palindrome.
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True
```

## 17. Implement a function that returns the length of the longest word in a sentence.
```python
def longest_word_length(sentence):
    return max(len(word) for word in sentence.split())

print(longest_word_length("Python programming is fun"))  # Output: 11
```

## 18. Demonstrate nested list indexing.
```python
nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])  # Output: 6
```

## 19. How do you convert a list of characters into a string?
```python
chars = ['H', 'e', 'l', 'l', 'o']
print("".join(chars))  # Output: "Hello"
```

## 20. Write code to remove duplicates from a list while preserving order.
```python
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 2]))  # Output: [1, 2, 3, 4]
```

## 21. Write a function that takes a list of tuples and sorts it by the second element of each tuple.
```python
def sort_by_second_element(tuples):
    return sorted(tuples, key=lambda x: x[1])

print(sort_by_second_element([(1, 3), (2, 1), (4, 2)]))  # Output: [(2, 1), (4, 2), (1, 3)]
```

## 22. Implement a program to flatten a nested list of arbitrary depth.
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]
```

## 23. Create a function that rotates a list to the right by k steps.
```python
def rotate(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

print(rotate([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
```

## 24. Given two strings, write a function that returns True if they are anagrams.
```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # Output: True
```

## 25. Create a function to split a list into chunks of a specified size.
```python
def chunk(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

print(chunk([1, 2, 3, 4, 5, 6], 2))  # Output: [[1, 2], [3, 4], [5, 6]]
```

## 26. Implement a function that merges two sorted lists into one sorted list.
```python
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```







# 🚀 Questions on Sequences in Python

## 1. Data Pipeline Validator

**Task**: Identify the longest pipeline and return pipelines taking more than a given threshold time.

```python
pipelines = [
    ("Data Ingestion", 30),
    ("Preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20)
]
threshold = 40

longest_pipeline = max(pipelines, key=lambda x: x[1])[0]
exceeding_pipelines = [p[0] for p in pipelines if p[1] > threshold]

print("Longest Pipeline:", longest_pipeline)
print("Pipelines exceeding threshold:", exceeding_pipelines)
```

## 2. Log File Parser

**Task**: Extract unique error codes from a log file.

```python
logs = """ERROR 404: Not Found
INFO: Connection established
ERROR 500: Internal Server Error
ERROR 404: Not Found
"""

error_codes = set(line.split()[1].strip(':') for line in logs.split('\n') if line.startswith("ERROR"))
print("Unique Error Codes:", list(error_codes))
```

## 3. Config File Reader

**Task**: Parse key-value pairs from a configuration string.

```python
config = "host=127.0.0.1;port=8080;mode=debug"
config_pairs = [tuple(pair.split('=')) for pair in config.split(';')]
print(config_pairs)
```

## 4. Social Media Data Cleaner

**Task**: Extract unique hashtags from a social media post.

```python
post = "Loving the new #Python course! #Coding #Python #Learning"
hashtags = list(set(word for word in post.split() if word.startswith('#')))
print(hashtags)
```

## 5. Secret Code Decoder

**Task**: Extract every third character from a string.

```python
secret_message = "hweollrolwd"
decoded_message = secret_message[::3]
print(decoded_message)
```

## 6. Inventory Tracker

**Task**: Find the product with the highest quantity.

```python
inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
]
most_stocked = max(inventory, key=lambda x: x[1])[0]
print(most_stocked)
```

## 7. Survey Data Analyzer

**Task**: Extract scores from a survey string and find min/max.

```python
survey_data = "5,3,4,1,2"
scores = list(map(int, survey_data.split(',')))
print("Max Score:", max(scores))
print("Min Score:", min(scores))
```

## 8. Access Control Manager

**Task**: Manage user access levels using lists and tuples.

```python
users = ["Alice", "Bob", "Charlie"]
roles = ("Admin", "Editor", "Viewer")
access = dict(zip(users, roles))
print(access)
```

## 9. Customer Support Ticket System

**Task**: Categorize tickets based on message length.

```python
message = "My account is locked, please help!"
length = len(message)
category = "Short" if length < 20 else "Medium" if length < 50 else "Long"
print("Category:", category)
```

## 10. Product Catalog Manager

**Task**: Find the product with the longest name.

```python
products = ["Laptop", "Smartphone", "Wireless Headphones"]
longest_product = max(products, key=len)
print(longest_product)
```

## 11. Sensor Data Analyzer

**Task**: Extract the last 10 sensor readings and calculate the average.

```python
sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
last_10 = sensor_readings[-10:]
average = sum(last_10) / len(last_10)
print("Average:", average)
```

## 12. Transaction Reverser

**Task**: Reverse the list of transactions.

```python
transactions = [100, -50, 200, -150, 50]
reversed_transactions = transactions[::-1]
print(reversed_transactions)
```

## 13. Log Formatter

**Task**: Format logs with timestamps.

```python
logs = ["System Boot", "Network Connected", "User Login"]
timestamp = "2025-03-20"
formatted_logs = [f"{timestamp}: {log}" for log in logs]
print(formatted_logs)
```

## 14. Pattern Generator

**Task**: Generate patterns with repetition.

```python
symbol = "*"
count = 5
pattern = " ".join([symbol] * count)
print(pattern)
```

## 15. Customer Feedback Analyzer

**Task**: Count keyword occurrences.

```python
feedback = "The product is excellent, absolutely excellent!"
count = feedback.lower().count("excellent")
print("'excellent' count:", count)
```

## 16. Sentence Index Finder

**Task**: Find the index of the first occurrence of "error".

```python
log = "INFO: All systems go. ERROR: Failed to start service."
index = log.lower().find("error")
print("Index:", index)
```

## 17. CSV Parser

**Task**: Parse CSV data into lists.

```python
csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
rows = [row.split(',') for row in csv_data.split('\n')]
print(rows)
```

## 18. Username Generator

**Task**: Generate usernames from full names.

```python
names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
usernames = [name.split()[0][0] + name.split()[1] for name in names]
print(usernames)
```

## 19. Chat Log Analyzer

**Task**: Count messages per user from chat logs.

```python
chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]
from collections import Counter
message_counts = Counter(log.split(':')[0] for log in chat_logs)
print(message_counts)
```

## 20. Data Compressor

**Task**: Compress recurring substrings.

```python
data = "abababababab"
substring = "ab"
count = data.count(substring)
print(f"'{substring}' repeated {count} times")
```

