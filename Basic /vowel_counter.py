text = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = sum(1 for char in text if char in vowels)
print(f"Vowel count: {count}")