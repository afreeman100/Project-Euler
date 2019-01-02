fSequence = fibonacciN 1000
answer = length fSequence

--create list of fibonacci numbers until one is n digits long
fibonacciN :: Int -> [Integer]
fibonacciN n = fibN n []
    where
        fibN n l                                                --numberOfDigits, fibonacciList
            | l == []               = fibN n ([1])              --base case 1
            | l == [1]              = fibN n ([1,1])            --base case 2
            | digits (head l) == n  = l                         --number has enough digits! Stop.
            | otherwise             = fibN n ((l!!0 + l!!1):l)  --next fibonacci number


--number of digits in a number
digits :: Integer -> Int
digits n
    | n `div` 10 == 0   = 1
    | otherwise         = digits(n `div` 10) + 1
