class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        import math
        val = math.log(num) / math.log(4)

        # 로그의 값이 정수여야지만 통과가능
        if val == int(val):
            return True
        return False
