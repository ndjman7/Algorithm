# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        levels = {}
        def find_level(node, level):

            if node is None:
                return

            if level not in levels:
                levels[level] = node.val
            else:
                levels[level] += node.val

            if node.left:
                find_level(node.left, level+1)

            if node.right:
                find_level(node.right, level+1)

            return

        find_level(root, 1)

        max_level = max_value = 0
        for level, value in levels.items():
            if max_value < value:
                max_value = value
                max_level = level

        return max_level
