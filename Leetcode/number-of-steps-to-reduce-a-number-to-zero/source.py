class Solution:
    def numberOfSteps (self, num: int) -> int:
        step = 0
        while num > 0:
            if num % 2:
                num -= 1
            else:
                num = int(num / 2)
            step += 1

        return step

