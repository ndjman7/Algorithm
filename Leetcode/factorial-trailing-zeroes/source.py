class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_fives = 0
        while n:
            num_fives += n/5
            n = n/5
        return num_fives
