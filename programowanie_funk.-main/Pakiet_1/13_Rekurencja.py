def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

number = 0
result = calculate_factorial(number)
print(f"Silnia z {number} wynosi {result}")
