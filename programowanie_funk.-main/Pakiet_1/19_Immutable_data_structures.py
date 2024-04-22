def add_to_tuple(original_tuple, value, index):
    temp_list = list(original_tuple)
    temp_list[index] = value
    return tuple(temp_list)

my_tuple = (1, 2, 3, 4, 5)
updated_tuple = add_to_tuple(my_tuple, 69, 0)

print(updated_tuple)
