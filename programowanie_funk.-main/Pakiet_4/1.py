def sum_of_evens(lst):
    """
    Funkcja zwraca sumę wszystkich parzystych liczb w liście.
    """
    return sum(x for x in lst if x % 2 == 0)

# Testowanie funkcji
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_evens(numbers)
print("Suma parzystych liczb:", result)
