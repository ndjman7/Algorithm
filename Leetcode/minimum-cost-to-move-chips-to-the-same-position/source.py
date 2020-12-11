class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        total_odd_value = total_even_value = 0

        for index in position:
            if index % 2 == 1:
                total_odd_value += 1
            else:
                total_even_value += 1

        if total_even_value < total_odd_value:
            return total_even_value
        else:
            return total_odd_value

