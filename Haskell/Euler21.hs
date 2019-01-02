amicable = [x | x<-[1..10000], isAmicable(x)]
answer = sum amicable

isAmicable :: Int -> Bool
isAmicable x = x==f2 && x/=f1
    where
        f1 = sum(factors x)
        f2 = sum(factors f1)

factors :: Int -> [Int]
factors x = 1:fact x 2
    where
        fact x f
            | f >= round (sqrt (fromIntegral  x))   = []
            | (mod x f) == 0                        = (div x f):(f:(fact (x) (f+1)))
            | otherwise                             = fact x (f+1)
