def rotate_list(lst, steps):

    if not lst:
        return []

    steps %= len(lst)

    rotated_list = lst[-steps:] + lst[:-steps]
    
    return rotated_list

my_list = [1, 2, 3, 4, 5, 6]
steps_to_rotate = 2
result = rotate_list(my_list, steps_to_rotate)
print("Lista po obrocie o", steps_to_rotate, "kroki w prawo:", result)
