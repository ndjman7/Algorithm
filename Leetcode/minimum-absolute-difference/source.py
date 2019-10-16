class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        answer = []
        arr = sorted(arr)
        min_val = 987654321

        for i in range(len(arr)-1):
            val = abs(arr[i] - arr[i+1])
            min_val = min(val, min_val)

        for i in range(len(arr)-1):
            if min_val == abs(arr[i] - arr[i+1]):
                answer.append([arr[i], arr[i+1]])

        return answer
