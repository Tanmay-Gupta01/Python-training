
import copy

original = {'a': [1, 2], 'b': [3, 4]}
shallow_copy = original.copy()

shallow_copy['a'].append(99)

print("Original after shallow copy change:", original)  

original = {'a': [1, 2], 'b': [3, 4]}
deep_copy = copy.deepcopy(original)
deep_copy['a'].append(99)

print("Original after deep copy change:", original)  

