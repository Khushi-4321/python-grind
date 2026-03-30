# Day 20 - Recursion: Power function
def recursive_power(base, exp):
    if exp == 0:
        return 1
    return base * recursive_power(base, exp - 1)

print(recursive_power(3, 4))