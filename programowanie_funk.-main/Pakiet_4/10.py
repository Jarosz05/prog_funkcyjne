def generate_permutations(lst):
    if len(lst) <= 1:
        return [lst]
    
    permutations = []
    
    for i in range(len(lst)):
        first_element = lst[i]
        
        remaining_elements = lst[:i] + lst[i+1:]
        
        for perm in generate_permutations(remaining_elements):
            permutations.append([first_element] + perm)
    
    return permutations

my_list = [1, 2, 3, 4]
permutations = generate_permutations(my_list)
print("Permutacje:", permutations)
