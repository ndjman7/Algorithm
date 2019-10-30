"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        answer = []

        def get_preorder_list(node):
            if node is None:
                return
            answer.append(node.val)

            for child in node.children:
                get_preorder_list(child)

        get_preorder_list(root)

        return answer
