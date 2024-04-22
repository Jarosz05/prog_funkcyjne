def add(x):
    def add_inner(y):
        return x + y
    return add_inner

add_partial = add(5)
result = add_partial(8)
print(result)
