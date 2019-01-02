import math


#return true if x is an abundant number
def isAbundant(x):
    factors = [1]
    for f in range(2,int(math.sqrt(x)+1)):
        if x%f==0:
            factors.append(f)
            if f**2 != x:
                factors.append(x//f)

    if sum(factors)>x:
        return True
    else:
        return False


#return true if x can be written as a sum of 2 abundant numbers
def abundantSum(x):
    for i in range(1, (x//2)+1):
        if isAbundant(i) and isAbundant(x-i):
            return True
    return False


n = 28123

#abundant numbers up to n
aNumbers = [x for x in range(1,n) if isAbundant(x)]

#numbers up to n that can't be made by summing 2 abundant numbers
sumList = [i for i in range(n) if not abundantSum(i)]

print(aNumbers)
print(sumList)
print(sum(sumList))