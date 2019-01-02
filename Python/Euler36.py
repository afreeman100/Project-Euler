import  math


def isPalindrome(x):
    w = list(str(x))
    wr = w[::-1]
    return w==wr


def toBinary(x):
    binary = 0
    power = int(math.log(x, 2))

    while x>0:
        if x-2**power >= 0:
            x -= 2**power
            binary += 10**power
        power -= 1

    return binary


pSum = 0
for i in range(1, 1000000):
    if isPalindrome(i) and isPalindrome(toBinary(i)):
        pSum += i

print(pSum)

