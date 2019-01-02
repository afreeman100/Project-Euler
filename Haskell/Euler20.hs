factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n*factorial(n-1)

sumDigits :: Integer -> Integer
sumDigits 0 = 0
sumDigits n = (n `mod` 10) + sumDigits (n `div` 10)

answer = sumDigits(factorial(100))
