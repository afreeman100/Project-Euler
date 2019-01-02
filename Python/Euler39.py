import  math


#calculate pythagorean triples up to n
def pythagTriples(n):
    p = []
    for i in range(3,n):
        for j in range(i,n):
            h = math.sqrt(i**2 + j**2)
            if h == int(h):
                p.append((i,j,int(h)))
    return p


#find number of pythagorean triples that give perimeter of p (if any)
def perimeterCount(p):
    count = 0
    for triple in pythagList:
        if sum(triple) == p:
            count+=1
    return count


#find perimeter up to p that gives max solutions
def maxSolutions(pMax):

    maxSolution = 0
    maxPerimeter = 0

    for p in range(3, pMax):
        solutions = perimeterCount(p)
        if solutions > maxSolution:
            maxSolution = solutions
            maxPerimeter = p

    return maxPerimeter



upTo = 1000
pythagList = pythagTriples(upTo)
print(maxSolutions(upTo))
