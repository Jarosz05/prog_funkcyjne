def find_max_min_diff(lst):

    if not lst:
        return None
    
    max_value = max(lst)
    min_value = min(lst)
    
    return max_value - min_value

numbers = [3, 7, 2, 9, 5, 1, 8]
result = find_max_min_diff(numbers)
print("Różnica między maksymalną a minimalną wartością:", result)
