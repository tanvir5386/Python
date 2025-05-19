a, b = 0, 1
n = int(input("Enter n: "))

for _ in range(n - 1):
    a, b = b, a + b

print(f"The {n}th Fibonacci number is: {a}")
