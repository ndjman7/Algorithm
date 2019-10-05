class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones = sorted(stones)
            result_stone = stones[-1] - stones[-2]

            del stones[-2]
            if result_stone:
                stones[-1] = result_stone
            else:
                del stones[-1]

        if stones:
            return stones[0]
        else:
            return 0

