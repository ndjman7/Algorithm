class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollors = 0
        ten_dollors = 0
        for bill in bills:
            if bill == 5:
                five_dollors += 1
            elif bill == 10:
                if five_dollors == 0:
                    return False
                five_dollors -= 1
                ten_dollors += 1
            elif bill == 20:
                if five_dollors >= 1 and ten_dollors >= 1:
                    ten_dollors -= 1
                    five_dollors -= 1
                elif five_dollors >= 3:
                    five_dollors -= 3
                else:
                    return False

        return True
