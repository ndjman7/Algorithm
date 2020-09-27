class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def find_value(n):
            if n < 2:
                return n
            if n == 2:
                return 1
            if cache.get(n):
                return cache[n]
            value = find_value(n-3) + find_value(n-2) + find_value(n-1)
            cache[n] = value
            return value
        return find_value(n)

