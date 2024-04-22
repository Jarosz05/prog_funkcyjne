def analyze_data(data):
    if isinstance(data, list):
        print("To jest lista zawierająca", len(data), "elementów.")
    elif isinstance(data, tuple):
        print("To jest krotka zawierająca", len(data), "elementów.")
    else:
        print("To jest inna struktura danych.")

my_list = [1, 2, 3, 4]
my_tuple = (4, 5, 6, 7)
my_dict = {"a": 1, "b": 2}

analyze_data(my_list)
analyze_data(my_tuple)
analyze_data(my_dict)
