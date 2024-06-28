--Contributed by Ron Watkins
module Main where

fib 0 = 0
fib 1 = 0
fib 2 = 1
fib n = (fib (n-2)) + (fib (n-1))


-- This part is related to the Input/Output and can be used as it is
-- Do not modify it
main = do
    input <- getLine
    print . fib . (read :: String -> Int) $ input
