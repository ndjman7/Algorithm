class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans = [0 for i in S]

        for i in range(len(S)):
            if i == 0:
                small_idx = 10000
            else:
                small_idx = ans[i-1] + 1

            if i == len(S) - 1:
                if S[i] == C:
                    idx = 0
                else:
                    idx = ans[i-1] + 1
            else:
                n_i = i
                idx = 0

                while True:
                    if S[n_i] == C:
                        break
                    if n_i == len(S) - 1:
                        idx = 10000
                        break
                    n_i += 1
                    idx += 1
            ans[i] = min(small_idx, idx)
        return ans
