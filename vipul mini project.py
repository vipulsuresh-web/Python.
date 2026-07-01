from datetime import datetime
import json
import os
import random

DB_FILE = "students_db.json"


# ==================== DATABASE FUNCTIONS ====================
def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def save_data(data):
    try:
        with open(DB_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except IOError:
        return False


# ==================== CORE PROFILE FUNCTIONS ====================
def generate_unique_id():
    """Generates a random, unique 6-digit Student ID string."""
    records = load_data()
    while True:
        new_id = str(random.randint(100000, 999999))
        if new_id not in records:
            return new_id


def add_student(name, age, course, phone):
    """Creates a new student record including verified phone number."""
    records = load_data()
    student_id = generate_unique_id()

    records[student_id] = {
        "name": name,
        "age": int(age),
        "course": course,
        "phone": phone,  # <-- Added phone number field
        "attendance": {}
    }
    save_data(records)
    return True, f"Student added successfully. Assigned ID: {student_id}"


def get_all_students():
    return load_data()


def search_student(student_id):
    records = load_data()
    return records.get(student_id, None)


def search_students_by_name(search_query):
    records = load_data()
    results = {}
    for sid, info in records.items():
        if search_query.lower() in info["name"].lower():
            results[sid] = info
    return results


def update_student(student_id, name=None, age=None, course=None, phone=None):
    records = load_data()
    if student_id not in records:
        return False, "Student not found."

    if name: records[student_id]["name"] = name
    if age: records[student_id]["age"] = int(age)
    if course: records[student_id]["course"] = course
    if phone: records[student_id]["phone"] = phone  # <-- Added phone update capability

    save_data(records)
    return True, "Student records updated successfully."


def delete_student(student_id):
    records = load_data()
    if student_id not in records:
        return False, "Student not found."

    del records[student_id]
    save_data(records)
    return True, "Student profile deleted successfully."


# ==================== ATTENDANCE TRACKER FUNCTIONS ====================
def mark_attendance(student_id, status):
    records = load_data()
    if student_id not in records:
        return False, "Student profile not found."

    if "attendance" not in records[student_id]:
        records[student_id]["attendance"] = {}

    today_date = datetime.today().strftime('%Y-%m-%d')
    records[student_id]["attendance"][today_date] = status
    save_data(records)
    return True, f"Attendance marked as '{status}' for today ({today_date})."


# ==================== INTERFACE FUNCTIONS ====================
def display_menu():
    print("\n" + "=" * 35)
    print("    STUDENT MANAGEMENT SYSTEM    ")
    print("=" * 35)
    print("1. Add New Student (Auto-ID)")
    print("2. View All Students")
    print("3. Search for Student by ID")
    print("4. Search for Student by Name")
    print("5. Update Student Profile")
    print("6. Delete Student Record")
    print("7. Mark Daily Attendance")
    print("8. View Attendance Report")
    print("9. Exit Application")
    print("=" * 35)


def run_menu():
    while True:
        display_menu()
        choice = input("Enter option (1-9): ").strip()

        if choice == "1":
            name = input("Enter Student Name: ").strip()
            age = input("Enter Age: ").strip()
            course = input("Enter Enrolled Course: ").strip()

            # Continuous validation loop for phone input
            while True:
                phone = input("Enter 10-digit Phone Number: ").strip()
                if len(phone) == 10 and phone.isdigit():
                    break
                print("⚠️ Invalid Phone Number! It must contain exactly 10 digits and numbers only.")

            if not (name and age and course) or not age.isdigit():
                print("⚠️ Invalid inputs! Profile fields cannot be blank. Age must be numeric.")
                continue

            success, msg = add_student(name, age, course, phone)
            print(f"✨ {msg}")

        elif choice == "2":
            students = get_all_students()
            if not students:
                print("📁 No records found in the database.")
            else:
                print(f"\n{'ID':<10} | {'Name':<15} | {'Course':<15} | {'Phone':<12}")
                print("-" * 65)
                for sid, info in students.items():
                    # Fallback phone format handling for legacy entries
                    phone_display = info.get("phone", "N/A")
                    print(f"{sid:<10} | {info['name']:<15} | {info['course']:<15} | {phone_display:<12}")

        elif choice == "3":
            sid = input("Enter Student ID to find: ").strip()
            student = search_student(sid)
            if student:
                print(
                    f"\n🔍 Record Found:\nID: {sid}\nName: {student['name']}\nAge: {student['age']}\nCourse: {student['course']}\nPhone: {student.get('phone', 'N/A')}")
            else:
                print("❌ No matching student profile found.")

        elif choice == "4":
            query = input("Enter student name to search: ").strip()
            if not query:
                print("⚠️ Search field cannot be empty.")
                continue

            results = search_students_by_name(query)
            if not results:
                print(f"❌ No student profiles match the name '{query}'.")
            else:
                print(f"\n🔍 Search Results for '{query}':")
                print(f"{'ID':<10} | {'Name':<15} | {'Course':<15} | {'Phone':<12}")
                print("-" * 65)
                for sid, info in results.items():
                    print(f"{sid:<10} | {info['name']:<15} | {info['course']:<15} | {info.get('phone', 'N/A'):<12}")

        elif choice == "5":
            sid = input("Enter Student ID to update: ").strip()
            if not search_student(sid):
                print("❌ Record not found.")
                continue
            name = input("Enter new name (leave blank to skip): ").strip() or None
            age_input = input("Enter new age (leave blank to skip): ").strip()
            age = int(age_input) if age_input.isdigit() else None
            course = input("Enter new course (leave blank to skip): ").strip() or None

            # Optional updated phone with validation loop
            phone = None
            while True:
                phone_input = input("Enter new phone number (leave blank to skip): ").strip()
                if not phone_input:
                    break
                if len(phone_input) == 10 and phone_input.isdigit():
                    phone = phone_input
                    break
                print("⚠️ Invalid Phone Number! It must contain exactly 10 digits.")

            success, msg = update_student(sid, name, age, course, phone)
            print(f"✨ {msg}")

        elif choice == "6":
            sid = input("Enter Student ID to delete: ").strip()
            success, msg = delete_student(sid)
            print(f"✨ {msg}")

        elif choice == "7":
            sid = input("Enter Student ID: ").strip()
            if not search_student(sid):
                print("❌ Student profile not found.")
                continue
            status_choice = input("Enter attendance status (1 for Present, 2 for Absent): ").strip()
            if status_choice == "1":
                status = "Present"
            elif status_choice == "2":
                status = "Absent"
            else:
                print("⚠️ Invalid choice. Attendance log aborted.")
                continue
            success, msg = mark_attendance(sid, status)
            print(f"✨ {msg}")

        elif choice == "8":
            sid = input("Enter Student ID to view history: ").strip()
            student = search_student(sid)
            if not student:
                print("❌ Student profile not found.")
                continue

            history = student.get("attendance", {})
            print(f"\n📊 Attendance Log for {student['name']} (ID: {sid}):")
            if not history:
                print("ℹ️ No attendance logs recorded yet.")
            else:
                print(f"{'Date':<15} | {'Status':<10}")
                print("-" * 30)
                for date, status in sorted(history.items()):
                    print(f"{date:<15} | {status:<10}")

        elif choice == "9":
            print("\nShutting down application. Goodbye!")
            break
        else:
            print("⚠️ Selection out of range. Pick between 1 and 9.")


if __name__ == "__main__":
    run_menu()