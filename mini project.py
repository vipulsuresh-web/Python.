students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        mark = input("Enter student mark: ")
        students[name] = mark
        print("Student added successfully!")

    elif choice == "2":
        if students:
        if students:
            print("\nStudent Records:")
            for name, mark in students.items():
                print("Name:", name, "| Mark:", mark)
        else:
            print("No records found.")

    elif choice == "3":
        name = input("Enter student name to search: ")
        if name in students:
            print("Mark:", students[name])
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
