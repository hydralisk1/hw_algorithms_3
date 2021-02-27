from divisors import find_divisors

def is_perfect_number(n):
    return True if sum(find_divisors(n)) == 2*n else False

# 6 is a perfect number
assert is_perfect_number(6)
# 10 is not a perfect number
assert not is_perfect_number(10)
# 28 is a perfect number
assert is_perfect_number(28)

# Find perfect numbers between 1 and 1000
for i in range(1, 1001):
    if is_perfect_number(i):
        print(f"{i} is a perfect number")