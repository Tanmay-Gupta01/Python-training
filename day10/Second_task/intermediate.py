# # 1 st question

# with open('day10\\Second_task\\input.txt', 'r') as file:
#     lines = file.readlines()

# # Filter out empty lines (after stripping whitespace)
# non_empty_lines = [line for line in lines if line.strip() != '']

# # Write the non-empty lines to cleaned.txt
# with open('day10\\Second_task\\cleaned.txt', 'w') as fp:
#     fp.writelines(non_empty_lines)


# # 2 nd question

# with open('day10\\Second_task\\input.txt', 'r+') as file:
#     lines = file.readlines()
#     modified_lines = []
#     for line in lines:
#         if line.strip() == 'Python':
#             modified_lines.append('PYTHON\n')
#         else:
#             modified_lines.append(line)
#     file.seek(0)
#     file.writelines(modified_lines)


# # 3 rd question

# with open('day10\\Second_task\\input.txt', 'r') as file:
#     lines = file.readlines()

# for i in range(len(lines)):
#     lines[i] = lines[i].upper()

# with open('day10\\Second_task\\output.txt', 'w') as fp:
#     fp.writelines(lines)


# # 4 th question

# scores = []
# with open('day10\\First_task\\students.txt','r')as file:
#     for line in file:
#         name, score = line.strip().split(',')
#         scores.append([name, int(score)])

# with open('day10\\Second_task\\report.txt','w')as fp:   
#     for name,score in scores:
#         if int(score) > 80:
#             fp.write(f'{name} - {score}\n')



# 5 th question

with open('day10\\Second_task\\input.txt', 'r') as file:
    lines = file.readlines()
    reverse_line = lines[::-1]
with open('day10\\Second_task\\reverse.txt', 'w') as fp:
    fp.writelines(reverse_line)  