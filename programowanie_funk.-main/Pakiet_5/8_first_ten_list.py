# Utworzenie listy zawierającej pierwsze 10 liczb kwadratowych
squared_numbers = [x ** 2 for x in range(1, 11)]
print("Pierwsze 10 liczb kwadratowych:", squared_numbers)

# Utworzenie listy długości słów z danej listy słów
words = ['apple', 'banana', 'orange', 'pineapple', 'kiwi']
word_lengths = [len(word) for word in words]
print("Długości słów:", word_lengths)
