# 3. Explain how indexing works in Python with an example.
# Indexing starts from `0` for positive values and `-1` for negative values.

string = "Python"
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

s = "Python Programming"
print(s[0:6])  # Output: Python


# 8. How would you reverse a string using slicing?

s = "Python"
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


# 13. Write code to split the sentence: "Learn Python, step by step!" into words.

sentence = "Learn Python, step by step!"
print(sentence.split())  # Output: ['Learn', 'Python,', 'step', 'by', 'step!']


# 14. Join a list `['Python', 'is', 'fun']` into a single string.

words = ['Python', 'is', 'fun']
print(" ".join(words))  # Output: "Python is fun"


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

print(longest_word_length("Python programming is fun"))  # Output: 11


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
