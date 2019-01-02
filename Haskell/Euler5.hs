--lowest common multiple of first n numbers
lm :: Int -> Int
lm n
    | n<=1  = 1
    | otherwise = lcm n (lm (n-1))



--This method works for 10, but is slooow when going up to 20
--lowest common multiple is first value that divides all numbers from 1 to 10
lowM = head [x | x<-[1,2..], (divisibleAll x [1..10])]
--returns True iff num is divisible by evey element of the factors list
divisibleAll :: Int -> [Int] -> Bool
divisibleAll num factors = all (\f-> (mod num f == 0)) factors
