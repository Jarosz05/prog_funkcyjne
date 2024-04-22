from itertools import product

list1 = ['A', 'B']
list2 = ['C', 'D']

for combination in product(list1, list2):
    print(combination)
