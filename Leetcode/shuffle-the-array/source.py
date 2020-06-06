class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        prev_nums = nums[:n]
        post_nums = nums[n:]
        for prev_num, post_num in zip(prev_nums, post_nums):
            answer.append(prev_num)
            answer.append(post_num)

        return answer
