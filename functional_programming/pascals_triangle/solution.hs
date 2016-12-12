-- Enter your code here. Read input from STDIN. Print output to STDOUT

fact :: Int -> Int
fact 0 = 1
fact n = n * fact (n-1)

binom :: Int -> Int -> Int
binom n r = (fact n) `div` (fact r * fact (n-r))

printRow n r
    | n == r = putStrLn "1"
    | otherwise = do
        putStr . show $ binom n r
        putStr " "
        printRow n (r+1)

pasq i n
    | i == n = return()
    | otherwise = do
        printRow i 0
        pasq (i+1) n
        
pas n = pasq 0 n

main = do
    input <- getLine
    pas . (read :: String -> Int) $ input