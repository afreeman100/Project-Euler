limit = 4000000

fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] < limit:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

filtered = filter(lambda x: x % 2 == 0, fibonacci)
print(sum(filtered))
