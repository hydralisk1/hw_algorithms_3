from divisors import find_divisors

def are_amicable_numbers(n1, n2):
    return True if sum(find_divisors(n1))-n1 == n2 and sum(find_divisors(n2))-n2 == n1 else False

# 220 and 284 are amicable numbers
assert are_amicable_numbers(220, 284)
# 10 and 12 are amicable numbers
assert not are_amicable_numbers(10, 12)