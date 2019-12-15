import math


def is_three_digit_pair(pair):
    return (99 < pair[0] < 1000) and (99 < pair[1] < 1000)


def factor_pairs(n):
    candidates = range(2, math.ceil((math.sqrt(n))))
    individual_factors = filter(lambda x: n % x == 0, candidates)
    return list(map(lambda factor: (factor, n // factor), individual_factors))


def has_three_digit_factor_pair(n):
    pairs = factor_pairs(n)
    three_digit_pairs = list(filter(is_three_digit_pair, pairs))
    return len(three_digit_pairs) > 0


def is_palindrome(n):
    as_string = str(n)
    return as_string == as_string[::-1]


def palindromes_in_range(from_, to_):
    return list(filter(is_palindrome, range(from_, to_)))


def palindromes_with_three_digit_factor_pair(from_, to_):
    palindromes = palindromes_in_range(from_, to_)
    return list(filter(has_three_digit_factor_pair, palindromes))


print(max(palindromes_with_three_digit_factor_pair(100 * 100, 999 * 999)))


# Or if you really want to do it in one line!:
# print(max(list(filter(lambda n: len(list(filter(lambda pair: (99 < pair[0] < 1000) and (99 < pair[1] < 1000), map(lambda x: (x, n // x), filter(lambda x: n % x == 0, range(2, math.ceil((math.sqrt(n))))))))) > 0, filter(lambda x: str(x) == str(x)[::-1], range(100*100, 999 * 999))))))
