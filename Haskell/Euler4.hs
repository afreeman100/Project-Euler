
--generates list such that each element x:
--     x is element of list containing all possible products of two 3-digit numbers
--     x is a palindrome
palindromes = [x | x<- (products [100..999] [100..999]), (show x) == (reverse (show x))]
pMax = show (maximum palindromes)

--  every element of xs multipled by every element in ys
products :: [Int] -> [Int] -> [Int]
products _ [] = []
products xs (y:ys) = (map (\x-> x*y) xs) ++ (products xs ys)
