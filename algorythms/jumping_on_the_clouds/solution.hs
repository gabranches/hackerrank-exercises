jump :: [Int] -> Int
jump [x0] = 0
jump [x0,x1] = 1
jump (x0:x1:x2:xs)
    | x1 == 0 && x2 == 0 || x1 == 1 = 1 + jump (x2:xs)
    | otherwise = 1 + jump (x1:x2:xs)

main :: IO ()
main = do
    n_temp <- getLine
    c_temp <- getLine
    let c = map read $ words c_temp :: [Int]
    print $ jump c 