text = "Hello, World!"
words = text.split()
print(words)


text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)


text = "   Hello, World!!!!!   "
print(text)
trimmed_text = text.strip().split()
print(trimmed_text)