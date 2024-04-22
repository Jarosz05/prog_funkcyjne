def map_nested(func, nested_list):

    return [map_nested(func, sublist) if isinstance(sublist, list) else func(sublist) for sublist in nested_list]

def square(x):
    return x ** 2

nested_list = [1, [2, 3], [4, [5, 6]]]
mapped_list = map_nested(square, nested_list)
print("Oryginalna lista:", nested_list)  
print("Zagnieżdżona lista:", mapped_list)
