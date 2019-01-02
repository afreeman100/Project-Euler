import math


def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


def rotations(x):

    r = []

    digits = len(str(x))
    d = (10**(digits-1))
    for i in range(0,digits):
        front = x//d
        x = x%d * 10 + front      #add front digit on end, shifting all other digits up by factor of 10
        r.append(x)

    return r


#return true if x is circular prime
def circularPrimes(x):

    #any even digits at all means cannot be circular prime
    num = str(x)
    for digit in num:
        if int(digit) % 2 == 0:
            return False

    #test all rotations
    r = rotations(x)
    for n in r:
        if not isPrime(n):
            return False

    return True


def countCircular(n):

    count = 0
    for i in range(1, n):
        if circularPrimes(i):
            count += 1
    return count


print(countCircular(1000000))