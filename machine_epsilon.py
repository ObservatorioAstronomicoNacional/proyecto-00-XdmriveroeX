import math
def calculate_machine_epsilon():
    epsilon = 1.0
    while 1.0 + epsilon / 2 > 1.0:
        epsilon /= 2
    return math.sqrt(epsilon)

epsilon_calc = calculate_machine_epsilon()
print(epsilon_calc)