class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n != 1:
            if n%3 == 0:
                n /= 3
            else:
                return False
        return True
