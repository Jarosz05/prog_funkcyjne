def filter_words_starting_with_a(words):
    return list(filter(lambda word: word.startswith('a'), words))

words = ['apple', 'banana', 'apricot', 'pear', 'avocado']
filtered_words = filter_words_starting_with_a(words)
print("Słowa zaczynające się na 'a':", filtered_words)

def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print("Kwadraty liczb:", squared_numbers)
