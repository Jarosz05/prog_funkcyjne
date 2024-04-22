def merge_dicts(*dicts):
    """
    Funkcja łączy dowolną liczbę słowników w jeden słownik, gdzie wartości dla powtarzających się kluczy są sumowane.
    """
    merged_dict = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict

# Testowanie funkcji
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 5, 'd': 7}
dict3 = {'a': 2, 'c': 4, 'e': 6}

result = merge_dicts(dict1, dict2, dict3)
print("Połączony słownik:", result)
