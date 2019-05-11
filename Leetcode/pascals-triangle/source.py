class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            ans = [[1], [1,1]]
            for idx in range(3, numRows + 1):
                l = [1]
                for x in range(1, idx-1):
                    l.append(ans[idx-1 -1][x-1] + ans[idx-1 -1][x])
                l.append(1)
                ans.append(l)
            return ans
