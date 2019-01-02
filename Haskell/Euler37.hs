import Factor

primes = primesTo 1000000

tPrimes = [p | p<-primes, tPrime p, p>9]
answer = sum tPrimes


removeRight :: Int -> [Int]
removeRight n
    | n < 10    = [n]
    | otherwise = n : (removeRight (div n 10))

removeLeft :: Int -> [Int]
removeLeft n
    | n < 10    = [n]
    | otherwise = n : (removeLeft (mod n ord))
        where ord = 10^(length (show n)-1)

tPrime :: Int -> Bool
tPrime x = (p1 && p2)
    where
        l1 = removeRight x
        l2 = removeLeft x
        p1 = all isPrime l1
        p2 = all isPrime l2
