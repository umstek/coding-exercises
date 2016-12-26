module Main where
    import Data.List
    main = do
        text <- getLine
        putStrLn $ nub text
