import math

# ---------- Temperature Conversion ----------

def celsius_to_fahrenheit():
    """Convert Celsius to Fahrenheit."""
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = (celsius * 9 / 5) + 32

    print(f"Result: {celsius}°C = {fahrenheit:.2f}°F")


def fahrenheit_to_celsius():
    """Convert Fahrenheit to Celsius."""
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5 / 9

    print(f"Result: {fahrenheit}°F = {celsius:.2f}°C")


# ---------- Area Calculations ----------

def area_of_circle():
    """Calculate the area of a circle."""
    radius = float(input("Enter radius of the circle: "))

    area = math.pi * radius ** 2

    print(f"Result: Area of circle (radius = {radius}) = {area:.2f} sq. units")


def area_of_rectangle():
    """Calculate the area of a rectangle."""
    length = float(input("Enter length of the rectangle: "))

    breadth = float(input("Enter breadth of the rectangle: "))

    area = length * breadth

    print(f"Result: Area of rectangle = {area:.2f} sq. units")


# ---------- Simple Interest ----------

def simple_interest():
    """Calculate simple interest."""
    principal = float(input("Enter Principal amount: Rs. "))

    rate = float(input("Enter Rate of interest (% per annum): "))

    time = float(input("Enter Time period (in years): "))

    interest = (principal * rate * time) / 100

    print(f"Result: Simple Interest = Rs. {interest:.2f}")


# ---------- BMI Calculation ----------

def calculate_bmi():
    """Calculate Body Mass Index."""
    weight = float(input("Enter weight in kg: "))

    height = float(input("Enter height in meters: "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Result: BMI = {bmi:.2f} ({category})")


# ---------- Display Menu ----------

def display_menu():
    """Display the toolkit menu."""

    print("\n========== PERSONAL UTILITY TOOL ==========")
    print("1. Celsius to Fahrenheit Conversion")
    print("2. Fahrenheit to Celsius Conversion")
    print("3. Calculate Area of Circle")
    print("4. Calculate Area of Rectangle")
    print("5. Calculate Simple Interest")
    print("6. Calculate Body Mass Index (BMI)")
    print("7. Exit")
    print("=============================================")


# ---------- Main Function ----------

def main():
    """Display menu and perform selected operation."""

    while True:

        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            celsius_to_fahrenheit()

        elif choice == "2":
            fahrenheit_to_celsius()

        elif choice == "3":
            area_of_circle()

        elif choice == "4":
            area_of_rectangle()

        elif choice == "5":
            simple_interest()

        elif choice == "6":
            calculate_bmi()

        elif choice == "7":
            print("Thank you for using the Personal Utility Tool. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


# ---------- Program Execution ----------

if __name__ == "__main__":
    main()