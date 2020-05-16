class Solution:
    def numTeams(self, rating: List[int]) -> int:
        answer = 0
        for a_index, a in enumerate(rating):
            for b_index, b in enumerate(rating[a_index+1:]):
                for c in rating[a_index+b_index+1:]:
                    if a < b < c:
                        answer += 1
                    if a > b > c:
                        answer += 1
        return answer

