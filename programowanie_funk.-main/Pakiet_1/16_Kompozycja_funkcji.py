def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

def compose(f, g):
    return lambda x: f(g(x))

add_then_multiply = compose(multiply_by_two, add_one)
print(add_then_multiply(20))