from math import sqrt

def find_divisors(n):
    if type(n) is not int or n <= 0:
        raise ValueError("The element has to be one of the natural numbers")

    result = []

    for i in range(1, int(sqrt(n)+1)):
        if n%i == 0:
            result.append(i)
            if n//i != i:
                result.append(n//i)

    return result