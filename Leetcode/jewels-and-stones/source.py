class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for j in J:
            for s in S:
                if j==s:
                    ans+=1

        return ans
