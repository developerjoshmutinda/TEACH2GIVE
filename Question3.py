# Write a program that takes an integer as input and returns true if the input is a power of two.
def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(8))  # returns True
print(is_power_of_two(6))  # returns False
