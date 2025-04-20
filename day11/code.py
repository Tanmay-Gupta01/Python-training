# Question 1

def department_salary_sort(data):
    result = {}
    for dept, emp, sal in data:
        result.setdefault(dept, []).append((emp, sal))
    for dept in result:
        result[dept].sort(key=lambda x: x[1], reverse=True)
    return result

data = [
    ('HR', 'Alice', 50000),
    ('HR', 'Bob', 60000),
    ('Tech', 'Charlie', 120000),
    ('Tech', 'Dave', 110000),
    ('Tech', 'Eve', 115000)
]

print(department_salary_sort(data))



# Question 2

def inverted_index(sentences):
    from collections import defaultdict
    index = defaultdict(set)
    for i, sentence in enumerate(sentences):
        for word in sentence.split():
            index[word].add(i)
    return {word: sorted(list(indices)) for word, indices in index.items()}

sentences = ["the quick brown fox", "jumps over the lazy dog", "the dog barked"]
print(inverted_index(sentences))



# Question 3

import copy

original = {'a': [1, 2], 'b': [3, 4]}
shallow_copy = original.copy()

shallow_copy['a'].append(99)

print("Original after shallow copy change:", original)  

original = {'a': [1, 2], 'b': [3, 4]}
deep_copy = copy.deepcopy(original)
deep_copy['a'].append(99)

print("Original after deep copy change:", original)  


# Question 4

def group_by_length(words):
    result = {}
    for word in words:
        result.setdefault(len(word), []).append(word)
    return result

words = ["hi", "hello", "hey", "bye", "thanks", "ok"]
print(group_by_length(words))



# Question 5

def merge_dicts(d1, d2):
    result = d1.copy()
    for key, val in d2.items():
        if key in result:
            result[key] = max(result[key], val)
        else:
            result[key] = val
    return result

d1 = {'a': 5, 'b': 10}
d2 = {'b': 7, 'c': 3}
print(merge_dicts(d1, d2))
