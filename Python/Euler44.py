import  math


#return nth pentagonal number
def Pn(n):
    return int(n*(3*n-1)/2)


#solve with quadratic formula. Pentagonal number iff solution is integer
def isPentagonal(x):
    c=-2*x
    s1 = (1 + math.sqrt(1 - 12 * c)) / 6
    return s1==int(s1)


def pentDifference():
    # pentagonal numbers up to n
    n = 10000

    for j in range(1, n + 1):
        for k in range(j + 1, n + 1):

            # pairs of pentagonal numbers up to n
            pj = Pn(j)
            pk = Pn(k)

            if isPentagonal(pj + pk) and isPentagonal(pk - pj):
                return pk - pj



print(pentDifference())