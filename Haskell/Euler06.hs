
difference :: Int -> Int
difference n = squareSums - sumSquares
    where
        sumSquares = sum (map (\x-> x*x) [1..n])
        squareSums = (sum [1..n])^2
