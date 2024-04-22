def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def read_large_file_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line


fibonacci = fibonacci_generator()
print("Pierwsze 10 liczb Fibonacciego:")
for _ in range(10):
    print(next(fibonacci), end=" ")

print("\n\nZawartość pliku 'large_file.txt':")
#for line in read_large_file_generator('large_file.txt'):
#    print(line.strip())
