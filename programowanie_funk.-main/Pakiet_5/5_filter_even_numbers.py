# Funkcja do filtrowania parzystych liczb
def filter_even_numbers(numbers):
    """
    Funkcja przyjmuje listę liczb i zwraca listę zawierającą tylko te liczby, które są parzyste.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))

# Testowanie funkcji filter_even_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print("Parzyste liczby:", even_numbers)

# Utworzenie funkcji lambda do obliczania pola prostokąta
rectangle_area = lambda length, width: length * width

# Testowanie funkcji lambda
length = 5
width = 10
area = rectangle_area(length, width)
print("Pole prostokąta:", area)
