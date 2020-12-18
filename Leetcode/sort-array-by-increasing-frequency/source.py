class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for num in nums:
            if not nums_dict.get(num):
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        sorted_nums_tuple = sorted(nums_dict.items(), key=lambda x: x[0], reverse=True)
        sorted_nums_tuple = sorted(sorted_nums_tuple, key=lambda x: x[1])

        answer = []
        for key, value in sorted_nums_tuple:
            for _ in range(value):
                answer.append(key)
        return answer

