# Define a dictionary to store student information
students = {}

# Function to add a student
def add_student():
  name = input("Enter student name: ")
  age = int(input("Enter student age: "))
  roll_number = int(input("Enter student roll number: "))
  students[roll_number] = {"name": name, "age": age}
  print("Student added successfully!")

# Function to search for a student
def search_student():
  roll_number = int(input("Enter student roll number to search: "))
  if roll_number in students:
    student_info = students[roll_number]
    print(f"Student Found:\n  Name: {student_info['name']}\n  Age: {student_info['age']}")
  else:
    print("Student not found.")

# Function to display all students
def display_students():
  if not students:
    print("No students found.")
    return
  print("Students:")
  for roll_number, student_info in students.items():
    print(f"  Roll Number: {roll_number}\n    Name: {student_info['name']}\n    Age: {student_info['age']}")

# Main program loop
while True:
  print("\nStudent Management System")
  print("1. Add Student")
  print("2. Search Student")
  print("3. Display All Students")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    add_student()
  elif choice == '2':
    search_student()
  elif choice == '3':
    display_students()
  elif choice == '4':
    print("Exiting Student Management System")
    break
  else:
    print("Invalid choice. Please try again.")

