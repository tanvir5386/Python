text = input("Enter text: ")
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word counts:", word_count)