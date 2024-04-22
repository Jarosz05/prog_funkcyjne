def filter_long_words(word_list):
    
    avg_length = sum(len(word) for word in word_list) / len(word_list)
    
    filtered_words = [word for word in word_list if len(word) > avg_length]
    return filtered_words

word_list = ["bułka", "dupa", "duuuuuupa", "grahamka", "chleb"]
filtered_words = filter_long_words(word_list)
print("Słowa o długości większej niż średnia długość:", filtered_words)
