class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        end = len(graph) - 1
        answer = []
        path = []
        def find_start_to_end(current_path):
            path.append(current_path)
            if current_path == end:
                right_path = path[:]
                answer.append(right_path)
            to_list = graph[current_path]
            for to in to_list:
                find_start_to_end(to)
            path.pop()

        find_start_to_end(0)
        return answer
