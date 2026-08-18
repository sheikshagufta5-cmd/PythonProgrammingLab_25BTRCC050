n = int(input("Enter number of consumers: "))

for i in range(1, n + 1):

    name = input(f"Consumer {i}: ")
    units = int(input("Units: "))

    if units == 0:
        print("0 units entered. Processing stopped.")
        break

    if units < 0:
        print(f"Invalid units for {name} - Skipped")
        continue

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = units * 3
    elif units <= 300:
        bill = units * 5
    else:
        bill = units * 7

    print(f"{name} - {units} units - Bill: Rs.{bill}")