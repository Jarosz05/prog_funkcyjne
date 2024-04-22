def generate_even_numbers():
    num = 0
    while True:
        yield num
        num += 3

generator = generate_even_numbers()

print(next(generator))
print(next(generator))
print(next(generator))
