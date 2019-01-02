

#generate up to xth row of pascal's triangle, count how many entries are greater than a million
def pascal(x):
    count = 0
    t = [[1]]
    for col in range(1, x+1):
        row = [1]
        for e in range(col-1):
            nextElement = t[col-1][e] + t[col-1][e+1]
            row.append(nextElement)

            if nextElement > 1000000:
                count += 1

        row.append(1)
        t.append(row)

    return count

print(pascal(100))