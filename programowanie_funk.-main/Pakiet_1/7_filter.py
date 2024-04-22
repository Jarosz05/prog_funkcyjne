words = ["apple", "banana", "orange", "kiwi", "pineapple", "grape", "watermelon"]

def filter_long_words(word):
    return len(word) > 5

long_words = list(filter(filter_long_words, words))

print(long_words)
