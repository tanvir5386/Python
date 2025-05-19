text = input("Enter text: ")
text = text.lower()
text = text.replace(' ', '')

if text == text[::-1]:
    print("Palindrome!")
else:
    print("Not palindrome")
