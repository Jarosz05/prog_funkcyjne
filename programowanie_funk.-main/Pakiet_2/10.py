def concat_strings(*args):
    return ' '.join(args)

strings1 = ["Hello", "world", "!"]
strings2 = ["Funkcja", "łącząca", "stringi", "w", "jeden", "ciąg."]

print(concat_strings(*strings1))
print(concat_strings(*strings2))
