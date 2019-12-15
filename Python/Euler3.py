import math


def is_prime(n):
    if n > 2 and n % 2 == 0:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def factors(n):
    candidates = range(2, math.ceil((math.sqrt(n))))
    f1 = list(filter(lambda x: n % x == 0, candidates))
    f2 = list(map(lambda x: n // x, f1))
    f1.extend(f2)
    return f1


def prime_factors(n):
    return list(filter(lambda x: is_prime(x), factors(n)))


print(prime_factors(600851475143))
