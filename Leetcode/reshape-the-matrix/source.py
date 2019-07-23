class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(nums)*len(nums[0]):
            return nums

        ans = []

        one_line = []
        for y in range(len(nums)):
            for x in range(len(nums[0])):
                one_line.append(nums[y][x])

        start_idx = 0
        for y in range(r):
            line = []
            for x in range(c):
                line.append(one_line[start_idx])
                start_idx += 1
            ans.append(line)

        return ans
