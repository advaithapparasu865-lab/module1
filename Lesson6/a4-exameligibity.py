from datetime import datetime

print("Exam Eligibility Check")
print("Date and time:", datetime.now())
print()

total_days = int(input("Enter total number of working days: "))
absent_days = int(input("Enter total number of days absent: "))

present_days = total_days - absent_days
percentage = (present_days / total_days) * 100

print()
print("Attendance percentage:", round(percentage, 2), "%")

if percentage < 75:
    print("You are not eligible to sit in the exam.")
else:
    print("You are eligible to sit in the exam.")