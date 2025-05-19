# number = int(input("Enter a number: "))
# print("Even" if number % 2 == 0 else "Odd")


# Check if a number is divisible by 5 or 7

# num = int(input("Enter a number: "))
# if num % 5 == 0 or num % 7 == 0:
#     print("Divisible by 5 or 7")
# else:
#     print("Not divisible by 5 or 7")



#  Check if a number is even and also greater than 100
num = int(input("Enter a number: "))

if num % 2 == 0 and num > 100:
    print("Even and greater than 100")
elif num % 2 == 0:
    print("Even but not greater than 100")
elif num > 100:
    print("Greater than 100 but not even")
else:
    print("Not even and not greater than 100")
