class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while True:
            if n == 0:
                break
            moc = n % 2
            n = int(n/2)
            if moc == 1:
                count += 1

        return count
