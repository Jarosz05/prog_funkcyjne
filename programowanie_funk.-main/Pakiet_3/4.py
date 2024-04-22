def remove_duplicates(input_list):
   
    seen = set()  
    output_list = []  
    
    for item in input_list:
        if item not in seen:
            output_list.append(item)
            seen.add(item)
    
    return output_list

my_list = [1, 2, 3, 2, 9, 9, 4, 3, 5, 6, 5]

print("Oryginalna lista:", my_list)  
print("Lista bez duplikatów:", remove_duplicates(my_list))  