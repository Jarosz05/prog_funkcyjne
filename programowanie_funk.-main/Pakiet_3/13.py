def split_list(lst, length):
  
    if not lst:
        return []

    return [lst[i:i+length] for i in range(0, len(lst), length)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublists = split_list(my_list, 3)
print("Podlisty o długości 3:", sublists)
