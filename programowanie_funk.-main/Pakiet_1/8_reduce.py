from functools import reduce

numbers = [1, 2, 3, 4, 5]
def add(x, y):
    return x + y

sum_of_numbers = reduce(add, numbers)

print(sum_of_numbers)
