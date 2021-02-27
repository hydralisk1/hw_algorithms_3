def factorial(n):
    if type(n) is not int or n < 0:
        raise ValueError("The element has to be an integer number greater than 0")

    return 1 if n == 0 else n * factorial(n-1)

# 0! = 1
assert factorial(0) == 1
# 2! = 2 * 1 = 2
assert factorial(2) == 2
# 5! = 5 * 4 * 3 * 2 * 1 = 120
assert factorial(5) == 120
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
assert factorial(6) == 720
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
assert factorial(10) == 3628800