
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n-1)

nCr :: Integer -> Integer -> Integer
nCr n r = fn `div` (nrf*rf)
    where
        fn  = factorial n
        nrf = factorial (n-r)
        rf  = factorial r

answer = 40 `nCr` 20
