#upper right diagonal is 1^2, 3^2, 5^2....n^2
#these can be used to calculate all the other diagonals.
#corners values of a square are given by:
#n^2 , n^2-(n-1) , n^2-2(n-1) , n^2-3(n-1)
#therefore sum of corners =   4n^2 - 6(n-1)
#sum corners from n, n-2, n-4...5, 3  (and add 1 for center)


size = 1001

diagonalSum = 1                             #+1 for center
for x in range(2, size+1, 2):               #2..n
        diagonalSum += 4*(x**2)-6*(x-1)     #using formula

print(diagonalSum)