def filter_even_values(dictionary):
    return {key: value for key, value in dictionary.items() if isinstance(value, int) and value % 2 == 0}

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
filtered_dict = filter_even_values(my_dict)
print("Słownik z liczbami parzystymi:", filtered_dict)
