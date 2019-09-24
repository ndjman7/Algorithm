class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        for move in moves:
            count[move] += 1

        return count['U'] == count['D'] and count['L'] == count['R']
