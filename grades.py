names = ["Arun", "Bala", "Charan", "Divya", "Esha"]

marks = [85, 72, 38, 105, 91]

valid_count = 0

for i, (name, mark) in enumerate(zip(names, marks), start=1):

    if mark < 0 or mark > 100:
        print(f"Invalid marks for {name} - Skipped")
        continue

    valid_count += 1

    if mark >= 80:
        result = "Excellent"
    elif mark >= 60:
        result = "Good"
    elif mark >= 40:
        result = "Average"
    else:
        result = "Fail"

    print(f"{i}. {name} - {mark} - {result}")

print(f"Total Valid Students: {valid_count}")