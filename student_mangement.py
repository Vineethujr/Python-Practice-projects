#Student Management System
#Creates a CSV file named students.csv
import csv

filename = "students.csv"


def load_students():
    students = []
    try:
        file = open(filename, "r", newline="")
        reader = csv.reader(file)
        for row in reader:
            students.append(row)
        file.close()
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    writer.writerows(students)
    file.close()


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    students = load_students()
    students.append([roll, name, marks])
    save_students(students)
    print("Student added successfully!")


def delete_student():
    roll = input("Enter roll number to delete: ")
    students = load_students()
    new_students = []
    found = False

    for row in students:
        if row[0] == roll:
            found = True
        else:
            new_students.append(row)

    save_students(new_students)

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def search_student():
    roll = input("Enter roll number to search: ")
    students = load_students()
    found = False

    for row in students:
        if row[0] == roll:
            print("Roll No:", row[0])
            print("Name:", row[1])
            print("Marks:", row[2])
            found = True
            break

    if not found:
        print("Student not found.")


def show_all_students():
    students = load_students()
    if not students:
        print("No students found.")
        return

    print("\nRoll No | Name | Marks")
    for row in students:
        print(row[0], "|", row[1], "|", row[2])


def show_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Show All Students")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        show_all_students()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-5.")