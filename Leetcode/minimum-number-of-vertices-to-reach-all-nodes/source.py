class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = dict()
        for edge in edges:
            visited[edge[1]] = True

        answer = []
        for v in range(n):
            if not visited.get(v):
                answer.append(v)

        return answer

