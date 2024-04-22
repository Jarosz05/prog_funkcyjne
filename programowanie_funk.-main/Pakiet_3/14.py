def count_unique_elements(lst):

    unique_elements = set(lst)
    return len(unique_elements)

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
unique_count = count_unique_elements(my_list)
print("Liczba unikalnych elementów:", unique_count)
