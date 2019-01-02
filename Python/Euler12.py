import  math


#returns nth triangular number
def triangleNum(n):
    tri = 0;
    while n>0:
        tri += n
        n -= 1
    return tri


#return the number of divisors n has (including 1 and n)
def numberOfDivisors(n):
    count = 0
    root = math.floor(math.sqrt(n))

    #if square number, prevent root from being counted twice
    if root**2 == n:
        count -=1

    for i in range(1,root+1):
        if n%i==0:
            count+=2
    return  count


count = 1

found = False
while not found:
    triNum = triangleNum(count)
    divisors = numberOfDivisors(triNum)
    count += 1
    if divisors > 500:
        print(triNum)
        found = True




