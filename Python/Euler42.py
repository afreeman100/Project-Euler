import math


def isTriangular(n):
    t = (-1+math.sqrt(1+8*n))/2
    return t == int(t)


f = open("Euler42Words.txt", 'r')
words = f.read().replace('"','').split(',')
print(words)

triCount = 0
for word in words:
    wordSum = 0
    for letter in word:
        wordSum += ord(letter)-64

    if isTriangular(wordSum):
        triCount += 1

print(triCount)


