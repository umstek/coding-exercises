solve :: Double -> Double
solve x = sum [ (power x i)/(factorial i) | i <- [0..9]]

factorial 0 = 1
factorial 1 = 1
factorial n = n * factorial(n-1)

power x p 
    | p == 0 = 1
    | p == 1 = x
    | otherwise = x * (power x (p-1))

main :: IO ()
main = getContents >>= mapM_ print. map solve. map (read::String->Double). tail. words
