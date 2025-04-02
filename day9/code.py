employees = {}

num_employees = int(input("Enter number of employees: "))

# Taking input for each employee
for _ in range(num_employees):
    name = input("\nEnter employee name: ")
    days = int(input(f"Enter number of days to track for {name}: "))
    attendance = []

    for day in range(1, days + 1):
        while True:
            status = input(f"Day {day} for {name} (P/A): ").upper()
            if status in ['P', 'A']:
                attendance.append(status)
                break
            else:
                print("Invalid input! Enter 'P' for Present or 'A' for Absent.")

    employees[name] = attendance

# Displaying Attendance Records
print("\nEmployee Attendance Records:")
for name, record in employees.items():
    print(f"{name}: {' '.join(record)}")
