class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        L = list(S)

        def append_ans(idx):
            if idx >= len(L):
                s = ''.join(L)
                if not s in ans:
                    ans.append(s)
                return

            if L[idx].isdigit():
                append_ans(idx+1)
            else:
                L[idx] = L[idx].lower()
                append_ans(idx+1)
                L[idx] = L[idx].upper()
                append_ans(idx+1)

        append_ans(0)
        return ans
