class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = 0
        length = len(arr)
        for i in range(1, length + 1, 2):
            for j in range(0, length):
                answer += sum(arr[j: i +j])
                if i+j == length:
                    break
        return answer

