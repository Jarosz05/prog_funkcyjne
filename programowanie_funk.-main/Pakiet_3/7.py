def flatten_list(nested_list):

    flattened_list = []
    for element in nested_list:
        if isinstance(element, list):
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    return flattened_list

nested_list = [1, [2, 3], [4, [5, 6]], 7, [8, [9, 10]]]
flat_list = flatten_list(nested_list)
print("Oryginalna lista:", nested_list)  
print("Spłaszczona lista:", flat_list)
