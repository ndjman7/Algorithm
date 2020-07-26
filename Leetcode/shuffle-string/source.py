class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = list(s[:])
        for idx, change_idx in enumerate(indices):
            answer[change_idx] = s[idx]
        return ''.join(answer)
