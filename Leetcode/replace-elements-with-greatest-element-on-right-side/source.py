class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        answer = []
        max_value = 0
        for index in reversed(range(len(arr)-1)):
            max_value = max(max_value, arr[index+1])
            answer.insert(0, max_value)

        answer.append(-1)

        return answer
