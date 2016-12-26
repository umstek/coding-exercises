module Main where
    main = do
        count_str <- getLine
        let n = read count_str :: Int
        let p = pascal n
        mapM (print_row) p

    print_row :: [Int] -> IO ()
    print_row p = putStrLn $ foldl1 (\ c x -> c ++ " " ++ x) [show i | i <- p]

    factorial :: Int -> Int
    factorial n
        | n == 0 = 1
        | n == 1 = 1
        | otherwise = n * factorial (n-1)

    ncr :: Int -> Int -> Int
    ncr n r = (factorial n) `div` ((factorial r) * (factorial (n-r)))

    pascal_row :: Int -> [Int]
    pascal_row n = [ ncr n i | i <- [0..n] ]

    pascal :: Int -> [[Int]]
    pascal n = [pascal_row i | i <- [0..n-1] ]