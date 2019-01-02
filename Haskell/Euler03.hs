--returns list of all prime factors of x
primeFactors :: Int -> [Int]
primeFactors x = primeFactors' x 2

primeFactors' :: Int -> Int -> [Int]
primeFactors' x f
    | x<=1                           = []                               --reached 1: all factors found
    | ((mod x f)==0) && (isPrime f)  = f:(primeFactors' (div x f) 2)    --prime factor found, divide and find new factors
    | otherwise                      = primeFactors' x (f+1)            --not a factor, check next



--returns true if x is prime
isPrime :: Int -> Bool
isPrime x = isPrime' x 2

isPrime' :: Int -> Int -> Bool
isPrime' num f
    | num==f           = True                   --num reached before factor found: prime
    | (mod num f)==0   = False                  --factor found: not prime
    | otherwise        = isPrime' num (f+1)     --not a factor: check next f
