"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def find_max_depth(node, depth):
            if node is None:
                return 0

            max_depth = depth
            for child in node.children:
                max_depth = max(max_depth, find_max_depth(child, depth+1))

            return max_depth

        return find_max_depth(root, 1)
