# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def find_depth(node):

            depth = 1
            if node is None:
                return 0
            if node.left is not None:
                depth = max(depth, 1 + find_depth(node.left))
            if node.right is not None:
                depth = max(depth, 1 + find_depth(node.right))

            return depth

        return find_depth(root)
