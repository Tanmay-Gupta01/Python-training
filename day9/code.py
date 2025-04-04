#  1. Employee Attendance Tracker

from datetime import date, timedelta

class Employee:
    """Manages employee records and attendance"""

    employee_list = []
    count = 1000  # Employee ID starts from 1001

    def create_employee(self, name, age):
        Employee.count += 1
        employee = {
            'Emp_id': Employee.count,
            'name': name,
            'age': age,
            'attendance': []  # Initialize empty attendance list
        }
        self.employee_list.append(employee)
        print(f"Employee created successfully! Employee ID: {employee['Emp_id']}")

    def display_employee_all(self):
        if not self.employee_list:
            print("No employees found.")
            return
        for employee in self.employee_list:
            print(f"Emp ID: {employee['Emp_id']}, Name: {employee['name']}, Age: {employee['age']}")

    def mark_attendance(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                last_seven_days = [date.today() - timedelta(days=i) for i in range(6, -1, -1)]
                attendance_data = {}

                for day in last_seven_days:
                    while True:
                        attendance = input(f"Enter attendance for {day} ('p' for present, 'a' for absent): ").strip().lower()
                        if attendance in ['p', 'a']:
                            attendance_data[str(day)] = attendance
                            break
                        print("Invalid input! Please enter 'p' or 'a'.")

                employee['attendance'].append(attendance_data)
                print("Attendance marked successfully!")
                return
        print("Employee ID not found!")

    def view_attendance(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                if not employee['attendance']:
                    print("No attendance records found for this employee.")
                    return
                print(f"Attendance for {employee['name']}:")
                for record in employee['attendance']:
                    for date, status in record.items():
                        print(f"{date}: {'Present' if status == 'p' else 'Absent'}")
                return
        print("Employee ID not found!")

    def get_employee_id(self, name):
        for employee in self.employee_list:
            if employee['name'].lower() == name.lower():
                return employee['Emp_id']
        print("Employee not found!")
        return None

    def delete_employee(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                self.employee_list.remove(employee)
                print("Employee deleted successfully!")
                return
        print("Employee ID not found!")

# --- Main Program ---
if __name__ == "__main__":
    employee_manager = Employee()

    while True:
        print("\nSelect an operation:")
        print("1. Create Employee")
        print("2. View All Employees")
        print("3. Mark Attendance")
        print("4. View Attendance")
        print("5. Delete Employee")
        print("6. Exit")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if user_choice == 1:
            name = input("Enter employee name: ").strip()
            try:
                age = int(input("Enter employee age: "))
                employee_manager.create_employee(name, age)
            except ValueError:
                print("Invalid age! Please enter a valid number.")

        elif user_choice == 2:
            employee_manager.display_employee_all()

        elif user_choice == 3:
            try:
                emp_id = int(input("Enter Employee ID to mark attendance: "))
                employee_manager.mark_attendance(emp_id)
            except ValueError:
                print("Invalid ID! Please enter a valid number.")

        elif user_choice == 4:
            try:
                emp_id = int(input("Enter Employee ID to view attendance: "))
                employee_manager.view_attendance(emp_id)
            except ValueError:
                print("Invalid ID! Please enter a valid number.")

        elif user_choice == 5:
            try:
                emp_id = int(input("Enter Employee ID to delete: "))
                employee_manager.delete_employee(emp_id)
            except ValueError:
                print("Invalid ID! Please enter a valid number.")

        elif user_choice == 6:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")




#  2. Password Strength Checker

def check_password_strength(password):
    """Evaluates the strength of a given password without using regex."""

    # Initialize criteria flags
    has_upper = has_lower = has_digit = has_special = False
    special_chars = "!@#$%^&*(),.?\":{}|<>"

    # Check each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Length check
    length_criteria = len(password) >= 8

    # Calculate strength score
    strength_score = sum([length_criteria, has_upper, has_lower, has_digit, has_special])

    # Determine password strength
    if strength_score == 5:
        return "Strong Password "
    elif strength_score >= 3:
        return "Medium Password "
    else:
        return "Weak Password "

# --- Main Program ---
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ").strip()
    result = check_password_strength(password)
    print(f"Password Strength: {result}")
