def fibonacci(n):
    if type(n) is not int or n < 0:
        raise ValueError("The element has to be an integer number greater than 0")

    return n if 0 <= n <= 1 else fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(10) == 55
assert fibonacci(20) == 6765