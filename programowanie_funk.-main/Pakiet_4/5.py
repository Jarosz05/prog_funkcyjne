def split_list(lst, max_length):
    return [lst[i:i+max_length] for i in range(0, len(lst), max_length)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_length = 2
result = split_list(my_list, max_length)
print("Podzielona lista:", result)
