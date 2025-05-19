try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    print(f"Result: {num1/num2}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid number input!")