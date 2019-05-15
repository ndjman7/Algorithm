class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        if math.sqrt(num).is_integer():
            return True
        return False
