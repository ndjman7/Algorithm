from functools import lru_cache

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        @lru_cache()
        def dp(tiles, length):
            if length == 1:
                return len(set(tiles))

            res = 0
            visited = {}
            for i, c in enumerate(tiles):
                if c in visited:
                    continue

                res += dp(tiles[:i] + tiles[i+1:], length - 1)
                visited[c] = True
            return res

        ans = 0
        for i in range(1, len(tiles)+1):
            ans += dp(tiles, i)
        return ans
