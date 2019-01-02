--to prevent having to rewrite code for problems involving primes and factors etc
module Factor where


nthPrime :: Int -> Int
nthPrime n = [x | x<-[1..], (isPrime x)] !! (n-1)


-- gives correct answer but bit slow. Could be improved using sieve
primesTo :: Int -> [Int]
primesTo n = [x | x<-[1..n], (isPrime x)]


--returns list of all prime factors of x
primeFactors :: Int -> [Int]
primeFactors x = pf x 2
    where
        pf x f
            | x<=1                           = []                    --reached 1: all factors found
            | ((mod x f)==0) && (isPrime f)  = f:(pf (div x f) 2)    --prime factor found, divide and find new factors
            | otherwise                      = pf x (f+1)            --not a factor, check next


--returns true if x is prime
isPrime :: Int -> Bool
isPrime num
    | num <= 1                              = False                 --prime numbers start at 2
    | (num==2)||(num==3)                    = True                  --2 or 3 are prime, but...
    | (num `mod` 2)==0 || (num `mod` 3)==0  = False                 --no other primes are divisible by 2 or 3
    | otherwise                             = isPrime' num 5        --now perform trial division
        where
            isPrime' num f
                | f > rootN          = True                         --no factors found: prime
                | (mod num f)==0     = False                        --all primes>3 are in form 6k(+/-)1: check 6k-1
                | (mod num (f+2))==0 = False                        --                                   check 6k+1
                | otherwise          = isPrime' num (f+6)           --not a factor: check next f+6
                where
                    rootN = round (sqrt (fromIntegral  num))


factors :: Int -> [Int]
factors x = fact x 2
    where
        fact x f
            | f > rootX                     = []                           --all factor pairs found
            | mod x f == 0 && (div x f)==f  = f:(fact (x) (f+1))           --square root, only add once
            | mod x f == 0                  = (div x f):(f:(fact (x) (f+1)))    --factor pair
            | otherwise                     = fact x (f+1)                 --not a factor, try next
                where
                    rootX = round (sqrt (fromIntegral  x))
