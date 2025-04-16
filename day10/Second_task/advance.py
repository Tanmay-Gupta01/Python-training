#  11th question

with open('day10\\\Second_task\\\server.log','r')as file:
    lines = file.readlines()
count = 0
with open('day10\\\Second_task\\\errors_only.log','w')as fp:
    for line in lines:
        if "ERROR" in line:
            fp.write(line)
            count += 1
    print(count)



# 12 th question

from collections import Counter
with open('day10\\\Second_task\\\input.txt','r') as file:
    lines = file.read().lower()

words = lines.split()
dictionary = Counter(words)
with open('day10\\\Second_task\\\frequency.txt','w') as fp:
    for word, frequency in dictionary.items():
        fp.write(f'{word} : {frequency}\n')



# 13 th question

with open('day10\\\Second_task\\\sales.csv', 'r') as file, open('day10\\\Second_task\\\high_sales.csv', 'w') as fp:
    lines = file.readlines()
    fp.write(lines[0])  

    for line in lines[1:]:
        date, customer, sales = line.strip().split(',')
        if int(sales) > 10000:
            fp.write(f'{date},{customer},{sales}\n')



# 14 th question

with open('day10\\Second_task\\input.txt','r') as file1, open('day10\\Second_task\\output.txt', 'r') as file2 ,open('day10\\Second_task\\frequency.txt','r') as file3, open('day10\\Second_task\\full_book.txt','w')as f:
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    lines3 = file3.readlines()
    f.write('--- From input.txt ---\n')
    f.writelines(lines1)
    f.write('\n--- From output.txt ---\n')
    f.writelines(lines2)
    f.write('\n--- From frequency.txt ---\n')
    f.writelines(lines3)


# 15 th question

import os 
path = "day10\Second_task"
all = os.listdir(path) 
files = [file for file in all if file.endswith('.txt') or file.endswith('.csv')]
print("txt and csv Files in '", path, "' :") 
print(files) 
