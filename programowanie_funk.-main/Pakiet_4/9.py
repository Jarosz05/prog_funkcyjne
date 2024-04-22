def apply_function_to_tuples(tuple_list, func):
    return [func(*t) for t in tuple_list]

def multiply(a, b):
    return a * b

tuples = [(1, 2), (3, 4), (5, 6)]
result = apply_function_to_tuples(tuples, multiply)
print("Lista po zastosowaniu funkcji:", result)
