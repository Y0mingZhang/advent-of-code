import Data.Char (chr, ord)

scoreRound :: Int -> Int
scoreRound 0 = 3
scoreRound 1 = 6
scoreRound _ = 0

scoreGameA :: [String] -> Int
scoreGameA ss = sum $ map helper ss
  where
    helper :: String -> Int
    helper s = scoreRound diff + yVal
      where
        x = ord $ head s
        y = ord $ s !! 2
        diff = mod (y - x - 20) 3
        yVal = y - ord 'X' + 1

scoreGameB :: [String] -> Int
scoreGameB ss = sum $ map helper ss
  where
    helper :: String -> Int
    helper s = scoreRound diff + yVal
      where
        x = ord $ head s
        diff = mod (ord (s !! 2) - ord 'Y' + 3) 3
        yVal = mod (x + diff + 3 - ord 'A') 3 + 1

main :: IO ()
main = do
  contents <- readFile "../data/2.in"
  let scoreA = scoreGameA $ lines contents
  print scoreA
  let scoreB = scoreGameB $ lines contents
  print scoreB
