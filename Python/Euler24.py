import itertools


def tuple_to_int(t):
    return int("".join(map(str, t)))


permutations = map(tuple_to_int, itertools.permutations(range(0, 10)))
ordered = sorted(permutations)
print(ordered[1000000 - 1])
