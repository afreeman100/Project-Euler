-- filter fibonacci numbers using conditions less than 400000 and even
evenSum = sum( filter (\x-> (x<=4000000)&&(mod x 2 ==0)) (fibonacci 50))

--returns list of first n fibonacci numbers, starting 1,1...
fibonacci :: Int -> [Int]
fibonacci n
    | n <= 0           = []
    | (n==1)||(n==2)   = 1 : f
    | otherwise        = (f!!0)+(f!!1) : f
    where f = fibonacci (n-1)
