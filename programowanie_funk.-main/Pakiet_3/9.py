def zip_with_index(lst):
    return [(element, index) for index, element in enumerate(lst)]

my_list = ['a', 'b', 'c', 'd', 'e']
result = zip_with_index(my_list)
print(result)
