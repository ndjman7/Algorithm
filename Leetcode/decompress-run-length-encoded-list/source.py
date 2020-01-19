class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums))[::2]:
            l = [
                nums[i+1]
                for _ 
                in range(nums[i])
            ]

            answer += l

        return answer
