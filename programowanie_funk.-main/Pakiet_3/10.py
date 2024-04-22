def cumulative_sum(lst):

    cumulative = []
    total = 0
    for num in lst:
        total += num
        cumulative.append(total)
    return cumulative

numbers = [1, 2, 3, 4, 5, 5.5]
result = cumulative_sum(numbers)
print("Suma skumulowana:", result)
