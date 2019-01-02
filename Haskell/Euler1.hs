
sumMultiples :: Int -> Int
sumMultiples n = sum (multiples n)

multiples :: Int -> [Int]
multiples n = l5 ++ (filter (\x -> (x `mod` 5)/=0) l3)
    where
        l3 = [0,3..n-1]
        l5 = [0,5..n-1]

--create list of multiples of 3 up to n (l3)
-- remove multiples of 5 from this list (with filter)
--  create list ofmultiples of 5 up to n
--   concatenate lists
--this prevents multiples of both (e.g. 15) being added twice
