class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        gold_medal = 'Gold Medal'
        silver_medal = 'Silver Medal'
        bronze_medal = 'Bronze Medal'

        # 각 값을 순서대로 정렬
        sort_nums = sorted(nums, reverse=True)

        # 해당 값을 key로 등수를 매김
        count = 1
        mapping = {}
        for num in sort_nums:
            mapping[num] = count
            count += 1

        # 원래 리스트에서 mapping에서 뽑아낸 rank를 기준으로 등수로 변경
        for idx, num in enumerate(nums):
            rank = mapping[num]

            if rank == 1:
                nums[idx] = gold_medal
            elif rank == 2:
                nums[idx] = silver_medal
            elif rank == 3:
                nums[idx] = bronze_medal
            else:
                nums[idx] = str(rank)

        return nums

