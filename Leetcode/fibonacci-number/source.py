class Solution:
    def fib(self, N: int) -> int:
        cache = {}
        def recursive_fib(val):
            if cache.get(val):
                return cache[val]
            else:
                if val < 2:
                    cache[val] = val
                    return cache[val]
                else:
                    cache[val] = recursive_fib(val-1) + recursive_fib(val-2)
                    return cache[val]

        return recursive_fib(N)
