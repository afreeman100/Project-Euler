splitDigits :: Int -> [Int]
splitDigits n
    | n == 0    = []
    | otherwise = (n `mod` 10) : splitDigits (n `div` 10)

factorial :: Int -> Int
factorial 0 = 1
factorial n = factorial (n-1) * n

factSum :: Int -> Bool
factSum n = n == sum f
    where
        f = map factorial (splitDigits n )

answer = sum [x | x<-[3..1000000], factSum x]
