collatz :: Int -> Int
collatz n
    | n `mod` 2==0  = n `div` 2
    | otherwise     = 3*n + 1

-- return the length of collatz chain from n to 1
chainLength :: Int -> Int
chainLength n
    | n==1      = 1
    | otherwise = 1 + chainLength(collatz n)

--number from 1 to n that produces the longest chain
findMax :: Int -> Int -> Int-> Int
findMax n maxChain maxN
    | n==1              = maxN
    | chain > maxChain  = findMax (n-1) chain    n
    | otherwise         = findMax (n-1) maxChain maxN
    where
        chain = chainLength n

maxChain = findMax 1000000 1 1
