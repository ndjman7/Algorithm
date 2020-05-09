class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            value = i*i
            if value == num:
                return True
            elif value > num:
                return False

