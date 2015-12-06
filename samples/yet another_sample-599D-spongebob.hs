{-
Codeforces

Problem 599D. Spongebob and Squares

@author yamaton
@date 2015-11-21
-}

import Control.Applicative
import Control.Monad
-- import Text.Printf
-- import System.IO (hPutStrLn, stderr)
import qualified Data.List as List
-- import qualified Data.Map as Map
-- import qualified Data.Set as Set
-- import qualified Data.Foldable as F
-- import qualified Data.Traversable as T


solve :: Int -> [(Int, Int)]
solve x = List.sort (partSols ++ flipped)
  where
    numer n = 6 * x - n * (n + 1) * (2 * n + 1) 
    denom n = 3 * n * (n + 1)
    candidates = id $! takeWhile (\(_, num, _) -> num >= 0) . map (\n -> (n, numer n, denom n)) $ [1..]
    partSols = [(n, n + p) | (n, num, den) <- candidates,
                             let p = num `div` den,
                             den * p == num]
    flipped = [(m, n) | (n, m) <- partSols, n < m]


main :: IO ()
main = do
    x <- read <$> getLine :: IO Int
    let result = solve x
    print (length result)
    mapM_ (putStrLn . (\(n, m) -> show n ++ " " ++ show m)) result
