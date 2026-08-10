

student_name = input("Enter Student Name: ")
student_usn = input("Enter Student USN: ")



MAX_MARKS_PER_SUBJECT = 100
NUM_SUBJECTS = 5

marks1 = float(input("Enter Marks in Subject 1 (out of 100): "))
marks2 = float(input("Enter Marks in Subject 2 (out of 100): "))
marks3 = float(input("Enter Marks in Subject 3 (out of 100): "))
marks4 = float(input("Enter Marks in Subject 4 (out of 100): "))
marks5 = float(input("Enter Marks in Subject 5 (out of 100): "))



total_marks = marks1 + marks2 + marks3 + marks4 + marks5

max_total_marks = MAX_MARKS_PER_SUBJECT * NUM_SUBJECTS

percentage = (total_marks / max_total_marks) * 100

average = total_marks / NUM_SUBJECTS



if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "RA"



print("\n========== STUDENT ACADEMIC PERFORMANCE REPORT ==========")

print(f"Student Name : {student_name}")
print(f"USN          : {student_usn}")

print("-----------------------------------------------------------")

print(f"{'Subject':<15}{'Marks (out of 100)':>20}")

print(f"{'Subject 1':<15}{marks1:>20.2f}")
print(f"{'Subject 2':<15}{marks2:>20.2f}")
print(f"{'Subject 3':<15}{marks3:>20.2f}")
print(f"{'Subject 4':<15}{marks4:>20.2f}")
print(f"{'Subject 5':<15}{marks5:>20.2f}")

print("-----------------------------------------------------------")

print(f"Total Marks    : {total_marks:.2f} / {max_total_marks}")
print(f"Percentage     : {percentage:.2f}%")
print(f"Average        : {average:.2f}")
print(f"Grade Obtained : {grade}")

print("===========================================================")