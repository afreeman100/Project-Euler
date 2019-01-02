diagonalSum :: Int -> Int
diagonalSum n
    | n==1      = 1
    | otherwise = diagonalSum (n-2) + (4*n^2 - 6*(n-1))

solution = diagonalSum 1001
