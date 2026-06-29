from datetime import datetime
import random
import os

# Generate Student ID
student_id = random.randint(1000, 9999)
print("Student ID:", student_id)

# Current date and time
now = datetime.now()
print("Date:", now.strftime("%d-%m-%Y"))
print("Time:", now.strftime("%H:%M:%S"))

# Create Reports folder if it doesn't exist
if not os.path.exists("Reports"):
    os.mkdir("Reports")

# Save a report
filename = f"Reports/Student_{student_id}.txt"

with open(filename, "w") as file:
    file.write("STUDENT MANAGEMENT SYSTEM\n")
    file.write("-------------------------\n")
    file.write(f"Student ID : {student_id}\n")
    file.write(f"Date : {now.strftime('%d-%m-%Y')}\n")
    file.write(f"Time : {now.strftime('%H:%M:%S')}\n")

print("Report Saved Successfully.")