def create_power_function(exponent):
    return lambda x: x ** exponent

square_function = create_power_function(2)
cube_function = create_power_function(3)

print("Kwadrat liczby 2:", square_function(2))
print("Sześcian liczby 3:", cube_function(3))
