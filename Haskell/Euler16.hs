sumDigits :: Integer -> Integer
sumDigits 0 = 0
sumDigits n = (n `mod` 10) + sumDigits (n `div` 10)

answer = sumDigits(2^1000)
