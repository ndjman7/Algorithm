class Solution:
    def returnHappy(self, n: int) -> int:
        sum = 0
        k = 0
        while True:
            if n / 10 == 0 and n % 10 == 0:
                break
            k = n % 10
            n /= 10
            sum = k * k
        return sum

    def isHappy(self, n: int) -> bool:
        hash = dict()
        while True:
            v = hash.get(n, None)
            print(n, v)
            if v is not None:
                return False
            if n == 1:
                return True
            prev_n = n
            n = self.returnHappy(prev_n)
            hash[prev_n] = n
        return False
