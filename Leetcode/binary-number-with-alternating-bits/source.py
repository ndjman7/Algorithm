class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        two = []
        while int(n / 2) > 0:
            two.append(str(n % 2))
            n /= 2
            n = int(n)
        two.append(str(n % 2))
        
        if len(two) == 1:
            return True
        c = two[0]
        for i in two[1:]:
            if c == i:
                return False
            c = i
        return True
