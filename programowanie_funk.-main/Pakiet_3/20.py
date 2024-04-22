def sum_of_squares_of_odds(lst):
    
    return sum(x ** 2 for x in lst if x % 2 != 0)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_of_squares_of_odds(numbers)
print("Suma kwadratów liczb nieparzystych:", result)

