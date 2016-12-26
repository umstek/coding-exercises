module Main where
    main = do
        count_str <- getLine
        let count = read count_str :: Int
        mapM consumeOne [0..count-1]


    rotate :: Int -> [Char] -> [Char]
    rotate pos xs = (drop pos xs) ++ (take pos xs) ++ [ ' ' ]

    rotateAll :: [Char] -> [[Char]]
    rotateAll xs = [ rotate i xs | i <- [1 .. (length xs)-1] ] ++ [ xs ]

    consumeOne :: Int -> IO ()
    consumeOne _ = do
        i_str <- getLine
        mapM putStr $ rotateAll i_str
        putStrLn ""