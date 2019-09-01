class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        alpha_dict = {}

        for i in range(26):
            alpha_dict[i] = widths[i]

        lines = 1
        one_line = 0
        for c in S:
            idx = ord(c) - 97

            if one_line + alpha_dict[idx] > 100:
                lines += 1
                one_line = alpha_dict[idx]

            else:
                one_line += alpha_dict[idx]

        return [lines, one_line]
