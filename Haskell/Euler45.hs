isTriangular :: Int -> Bool
isTriangular t = t == ttn
    where
        ttn =(tn*(tn + 1)) `div` 2
        tn  = quadratic 1 1 ((-2)*t)

isPentagonal :: Int -> Bool
isPentagonal p = p == ppn
    where
        ppn = (pn*(3*pn - 1)) `div` 2
        pn  = quadratic 3 (-1) ((-2)*p)

isHexagonal :: Int -> Bool
isHexagonal h = h == hhn
    where
        hhn = hn*(2*hn - 1)
        hn  = quadratic 2 (-1) (-h)

quadratic :: Int -> Int -> Int -> Int
quadratic a b c = ((-b) + round (sqrt (fromIntegral  (b^2 - 4*a*c)))) `div` (2*a)

--list of all numbers that are triangular, pentagonal and hexagonal
nums = [x | x<-[1..], isTriangular x, isPentagonal x, isHexagonal x]
answer = nums!!2
