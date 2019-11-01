"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        answer = []

        def get_post_order_list(node):

            if node is None:
                return

            for child in node.children:
                get_post_order_list(child)

            answer.append(node.val)

        get_post_order_list(root)

        return answer
