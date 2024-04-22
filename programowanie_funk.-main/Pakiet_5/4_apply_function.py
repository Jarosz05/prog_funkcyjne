def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def apply_operation(operation, x, y):
    """
    Funkcja przyjmuje inną funkcję jako argument i zastosowuje ją do podanych argumentów x i y.
    """
    return operation(x, y)

# Wywołanie funkcji apply_operation z różnymi operacjami
result_addition = apply_operation(add, 5, 3)
print("Wynik dodawania:", result_addition)

result_subtraction = apply_operation(subtract, 10, 4)
print("Wynik odejmowania:", result_subtraction)
