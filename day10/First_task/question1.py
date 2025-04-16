import csv

scores = []
avg =0

with open('day10\\First_task\\students.txt', 'r') as file:
    for line in file:
        name, score = line.strip().split(',')
        scores.append([name, int(score)])


for i in scores:
    avg +=i[1]
average = avg/len(scores)


with open('day10\\First_task\\top_students.txt','w') as file2:
    for name,score in scores:
        if average<score :
            file2.write(f"{name} : {score}\n")
    # print(file2.read)

with open('day10\\First_task\\top_student.csv','a', newline='') as csvfile :
    writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Score'])
    if csvfile.tell() == 0:  # Write header only if file is empty
            writer.writeheader()
            for name,score in scores:
                 if average<score :
                     writer.writerow({'Name': name, 'Score': score})

with open('day10\\First_task\\top_student.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)