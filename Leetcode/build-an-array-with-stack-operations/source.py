class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        num = 1
        for command in target:
            while num < command:
                answer.append("Push")
                answer.append("Pop")
                num += 1

            answer.append("Push")
            num += 1
        return answer

