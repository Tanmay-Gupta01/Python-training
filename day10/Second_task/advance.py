# #  11th question

# with open('day10\\Second_task\\server.log','r')as file:
#     lines = file.readlines()
# count = 0
# with open('day10\\Second_task\\errors_only.log','w')as fp:
#     for line in lines:
#         if "ERROR" in line:
#             fp.write(line)
#             count += 1
#     print(count)

# 12 th question

from collections import Counter
with open('day10\\Second_task\\input.txt','r') as file:
    lines = file.read().lower()

words = lines.split()
dictionary = Counter(words)
with open('day10\\Second_task\\frequency.txt','w') as fp:
    for word, frequency in dictionary.items():
        fp.write(f'{word} : {frequency}\n')