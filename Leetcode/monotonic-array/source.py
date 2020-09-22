class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        sign = None
        length = len(A)
        if length == 1:
            return True

        for index in range(length-1):
            next_index = index + 1
            new_sign = A[next_index] - A[index]

            if new_sign > 0:
                if sign:
                    if sign != '+':
                        return False
                else:
                    sign = '+'

            elif new_sign < 0:
                if sign:
                    if sign != '-':
                        return False
                else:
                    sign = '-'

        return True

