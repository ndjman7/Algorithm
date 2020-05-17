import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        answer = 0
        s_c = collections.Counter(s)
        t_c = collections.Counter(t)
        for key, value in t_c.items():
            change_value = s_c.get(key)
            if change_value:
                if value - change_value > 0:
                    answer += value - change_value
            else:
                answer += value

        return answer
