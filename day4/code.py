# 3. Explain how indexing works in  with an example.
# Indexing starts from `0` for positive values and `-1` for negative values.

string = ""
print(string[0])   # Output: P
print(string[-1])  # Output: n


# 4. Write code to access the last character of a string.

s = "Hello"
print(s[-1])  # Output: o


# 5. Create a list of numbers and access the third element.

numbers = [10, 20, 30, 40, 50]
print(numbers[2])  # Output: 30


# 6. What is the result of `len([1, [2, 3], 4])` and why?

# Output: `3` because the list contains three elements: `1`, `[2,3]`, and `4`.

# 7. Explain slicing with a practical example.

s = " Programming"
print(s[0:6])  # Output: 


# 8. How would you reverse a string using slicing?

s = ""
print(s[::-1])  # Output: nohtyP


# 9. Demonstrate list concatenation and repetition with examples.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Concatenation Output: [1, 2, 3, 4, 5, 6]
print(list1 * 2)      # Repetition Output: [1, 2, 3, 1, 2, 3]


# 10. Write code to count the occurrences of an element in a list.

lst = [1, 2, 2, 3, 4, 2]
print(lst.count(2))  # Output: 3


# 11. What will `my_tuple = (1, 2, 3); print(my_tuple[1:])` output?
# # Output: `(2, 3)`

# 12. Explain the difference between `list.append()` and `list.extend()`.
# - `append(x)`: Adds `x` as a single element.
# - `extend(iterable)`: Adds elements of `iterable` individually.


lst = [1, 2]
lst.append([3, 4])  # Output: [1, 2, [3, 4]]
lst = [1, 2]
lst.extend([3, 4])  # Output: [1, 2, 3, 4]


# 13. Write code to split the sentence: "Learn , step by step!" into words.

sentence = "Learn , step by step!"
print(sentence.split())  # Output: ['Learn', ',', 'step', 'by', 'step!']


# 14. Join a list `['', 'is', 'fun']` into a single string.

words = ['', 'is', 'fun']
print(" ".join(words))  # Output: " is fun"


# 15. Given a list `numbers = [1, 2, 2, 3, 4, 2]`, find the index of the first `2`.

numbers = [1, 2, 2, 3, 4, 2]
print(numbers.index(2))  # Output: 1


# 16. Write code to check if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True


# 17. Implement a function that returns the length of the longest word in a sentence.

def longest_word_length(sentence):
    return max(len(word) for word in sentence.split())

print(longest_word_length(" programming is fun"))  # Output: 11


# 18. Demonstrate nested list indexing.

nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])  # Output: 6


# 19. How do you convert a list of characters into a string?

chars = ['H', 'e', 'l', 'l', 'o']
print("".join(chars))  # Output: "Hello"


# 20. Write code to remove duplicates from a list while preserving order.

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 2]))  # Output: [1, 2, 3, 4]


# 21. Write a function that takes a list of tuples and sorts it by the second element of each tuple.

def sort_by_second_element(tuples):
    return sorted(tuples, key=lambda x: x[1])

print(sort_by_second_element([(1, 3), (2, 1), (4, 2)]))  # Output: [(2, 1), (4, 2), (1, 3)]


# 22. Implement a program to flatten a nested list of arbitrary depth.

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]


# 23. Create a function that rotates a list to the right by k steps.

def rotate(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

print(rotate([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]


# 24. Given two strings, write a function that returns True if they are anagrams.

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # Output: True


# 25. Create a function to split a list into chunks of a specified size.

def chunk(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

print(chunk([1, 2, 3, 4, 5, 6], 2))  # Output: [[1, 2], [3, 4], [5, 6]]


# 26. Implement a function that merges two sorted lists into one sorted list.

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]





# 🚀 Questions on Sequences in 

## 1. Data Pipeline Validator

# **Task**: Identify the longest pipeline and return pipelines taking more than a given threshold time.


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


## 2. Log File Parser

# **Task**: Extract unique error codes from a log file.


logs = """ERROR 404: Not Found
INFO: Connection established
ERROR 500: Internal Server Error
ERROR 404: Not Found
"""

error_codes = set(line.split()[1].strip(':') for line in logs.split('\n') if line.startswith("ERROR"))
print("Unique Error Codes:", list(error_codes))


## 3. Config File Reader

# **Task**: Parse key-value pairs from a configuration string.


config = "host=127.0.0.1;port=8080;mode=debug"
config_pairs = [tuple(pair.split('=')) for pair in config.split(';')]
print(config_pairs)


## 4. Social Media Data Cleaner

# **Task**: Extract unique hashtags from a social media post.


post = "Loving the new # course! #Coding # #Learning"
hashtags = list(set(word for word in post.split() if word.startswith('#')))
print(hashtags)


## 5. Secret Code Decoder

# **Task**: Extract every third character from a string.


secret_message = "hweollrolwd"
decoded_message = secret_message[::3]
print(decoded_message)


## 6. Inventory Tracker

# **Task**: Find the product with the highest quantity.


inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
]
most_stocked = max(inventory, key=lambda x: x[1])[0]
print(most_stocked)


## 7. Survey Data Analyzer

# **Task**: Extract scores from a survey string and find min/max.


survey_data = "5,3,4,1,2"
scores = list(map(int, survey_data.split(',')))
print("Max Score:", max(scores))
print("Min Score:", min(scores))


## 8. Access Control Manager

# **Task**: Manage user access levels using lists and tuples.


users = ["Alice", "Bob", "Charlie"]
roles = ("Admin", "Editor", "Viewer")
access = dict(zip(users, roles))
print(access)


## 9. Customer Support Ticket System

# **Task**: Categorize tickets based on message length.


message = "My account is locked, please help!"
length = len(message)
category = "Short" if length < 20 else "Medium" if length < 50 else "Long"
print("Category:", category)


## 10. Product Catalog Manager

# **Task**: Find the product with the longest name.


products = ["Laptop", "Smartphone", "Wireless Headphones"]
longest_product = max(products, key=len)
print(longest_product)


## 11. Sensor Data Analyzer

# **Task**: Extract the last 10 sensor readings and calculate the average.


sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
last_10 = sensor_readings[-10:]
average = sum(last_10) / len(last_10)
print("Average:", average)


## 12. Transaction Reverser

# **Task**: Reverse the list of transactions.


transactions = [100, -50, 200, -150, 50]
reversed_transactions = transactions[::-1]
print(reversed_transactions)


## 13. Log Formatter

# **Task**: Format logs with timestamps.


logs = ["System Boot", "Network Connected", "User Login"]
timestamp = "2025-03-20"
formatted_logs = [f"{timestamp}: {log}" for log in logs]
print(formatted_logs)


## 14. Pattern Generator

# **Task**: Generate patterns with repetition.


symbol = "*"
count = 5
pattern = " ".join([symbol] * count)
print(pattern)


## 15. Customer Feedback Analyzer

# **Task**: Count keyword occurrences.


feedback = "The product is excellent, absolutely excellent!"
count = feedback.lower().count("excellent")
print("'excellent' count:", count)


## 16. Sentence Index Finder

# **Task**: Find the index of the first occurrence of "error".


log = "INFO: All systems go. ERROR: Failed to start service."
index = log.lower().find("error")
print("Index:", index)


## 17. CSV Parser

# **Task**: Parse CSV data into lists.


csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
rows = [row.split(',') for row in csv_data.split('\n')]
print(rows)


## 18. Username Generator

# **Task**: Generate usernames from full names.


names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
usernames = [name.split()[0][0] + name.split()[1] for name in names]
print(usernames)


## 19. Chat Log Analyzer

# **Task**: Count messages per user from chat logs.


chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]
from collections import Counter
message_counts = Counter(log.split(':')[0] for log in chat_logs)
print(message_counts)


## 20. Data Compressor

# **Task**: Compress recurring substrings.


data = "abababababab"
substring = "ab"
count = data.count(substring)
print(f"'{substring}' repeated {count} times")


