def calculator():
    num1 = float(input("First number: "))
    op = input("Operator (+-*/): ")
    num2 = float(input("Second number: "))
    
    if op == '+': return num1 + num2
    if op == '-': return num1 - num2
    if op == '*': return num1 * num2
    if op == '/': return num1 / num2 if num2 != 0 else "Error"
    return "Invalid operator"

print("Result:", calculator())