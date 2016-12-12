--Contributed by Ron Watkins
module Main where

fibSeq = 1 : 1 : [x + y | (x, y) <- zip fibSeq (tail fibSeq)]

fib n = fibSeq !! (n - 2)

-- This part is related to the Input/Output and can be used as it is
-- Do not modify it
main = do
    input <- getLine
    print . fib . (read :: String -> Int) $ input
