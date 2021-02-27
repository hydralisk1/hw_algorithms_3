def digital_root(n):
    if type(n) is not int or n <= 0:
        raise ValueError("The element has to be one of the natural numbers")
    
    result = n%10 + digital_root(n//10) if n >= 10 else n

    return result if result < 10 else digital_root(result)

# 362093 = 3 + 6 + 2 + 0 + 9 + 3 = 23 = 2 + 3 = 5
assert digital_root(362093) == 5
# 1048576 = 1 + 0 + 4 + 8 + 5 + 7 + 6 = 31 = 3 + 1 = 4
assert digital_root(1048576) == 4
# 65535 = 6 + 5 + 5 + 3 + 5 = 24 = 2 + 4 = 6
assert digital_root(65535) == 6
# 9999999 = 9 + 9 + 9 + 9 + 9 + 9 + 9 = 63 = 6 + 3 = 9
assert digital_root(9999999) == 9