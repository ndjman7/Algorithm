"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
import queue

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        answer = []
        q = queue.Queue()

        def in_order(node, level):
            q.put((node, level))
            while not q.empty():
                node, level = q.get()
                try:
                    answer[level]
                except IndexError:
                    answer.append([])

                answer[level].append(node.val)

                for child in node.children:
                    q.put((child, level+1))

        if root:
            in_order(root, 0)

        return answer
