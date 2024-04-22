def apply_function_to_list(lst, func):
    return [func(x) for x in lst]

#funkcja 
def square(x):
    return x ** 2

original_list = [1, 2, 3, 4, 5]
result_list = apply_function_to_list(original_list, square)
print("po zastosowaniu funkcji:", result_list)
