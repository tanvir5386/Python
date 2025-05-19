# ফ্যাক্টরিয়াল হলো একটি সংখ্যার নিচের সব সংখ্যার গুণফল
# যেমন: 5! = 5 x 4 x 3 x 2 x 1 = 120
# রিকার্সিভ ফাংশন ব্যবহার করে ফ্যাক্টরিয়াল বের করা

# def factorial(n):
#     result = 1
#     for i in range(2, n+1):
#         result *= i
#     return result

# num = int(input("Enter a number: "))
# print(f"{num}! = {factorial(num)}")


# Strong Number: এমন সংখ্যা যার অঙ্কগুলোর ফ্যাক্টরিয়ালের যোগফল সংখ্যাটির সমান হয়
# যেমন: 145 = 1! + 4! + 5! = 145

def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += factorial(digit)
    temp //= 10

print("Strong Number" if sum_fact == num else "Not a Strong Number")
