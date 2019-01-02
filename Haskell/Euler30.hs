splitDigits :: Int -> [Int]
splitDigits n
    | n == 0    = []
    | otherwise = (n `mod` 10) : splitDigits (n `div` 10)


isPowerSum :: Int -> Int -> Bool
isPowerSum n p = n == sum (map (\x-> x^p) (splitDigits n))

answer = sum [x | x<-[2..1000000], isPowerSum x 5]
