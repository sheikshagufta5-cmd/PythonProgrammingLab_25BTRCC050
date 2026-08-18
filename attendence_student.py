names = ["Anu", "Bharath", "Chitra", "Deepak", "Farah"]

attendance = [92, 68, 85, 45, 78]

marks = [88, 55, 76, 32, 91]

eligible_count = 0

for i, (name, att, mark) in enumerate(zip(names, attendance, marks), start=1):

    if att < 0 or att > 100 or mark < 0 or mark > 100:
        print(f"Invalid data for {name} - Skipped")
        continue

    if att >= 75:
        eligible_count += 1

        if mark >= 80:
            grade = "Distinction"
        elif mark >= 60:
            grade = "First Class"
        elif mark >= 40:
            grade = "Pass"
        else:
            grade = "Fail"

        print(f"{i}. {name} - Attendance: {att}% - Marks: {mark} - {grade}")

    else:
        print(f"{i}. {name} - Attendance: {att}% - Not Eligible")

print(f"Total Eligible Students: {eligible_count}")