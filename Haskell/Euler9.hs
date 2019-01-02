--This works but is painfully slow
result = head [(x*y*z) | x<-[1..1000], y<-[1..1000], z<-[1..1000], (x^2 + y^2 == z^2), (x+y+z == 1000)]


--A better way:

answer = product (head(sumTo 1000))

--returns all pythagorean triples that sum to n. Therefore only need triples up to n
sumTo :: Int -> [[Int]]
sumTo n = filter (\t -> sum(t)==n) (getTriples n)


--return pythagorean triples up to n
getTriples :: Int -> [[Int]]
getTriples n = [[x, y, z] | x<-[1..n], y<-[1..n], z<-[root (x^2 + y^2)], (isPair x y)]

--does a pair (x,y )form a pythagorean triple (x,y,z)
--if (x^2 + y^2) does not give a square number then no
isPair :: Int -> Int -> Bool
isPair x y
    | x >= y    = False
    | otherwise = isSquare (x^2 + y^2)


--returns true iff x is a square number
isSquare :: Int -> Bool
isSquare n = (n==(root n)^2)


root :: Int -> Int
root n = round (sqrt (fromIntegral  n))
