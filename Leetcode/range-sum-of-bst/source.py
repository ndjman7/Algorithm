# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        answer = 0
        def find_range_value(node):
            nonlocal answer
            if node is None:
                return

            if L <= node.val <= R:
                answer += node.val

            if node.left and L < node.val:
                find_range_value(node.left)

            if node.right and node.val < R:
                find_range_value(node.right)

            return

        find_range_value(root)
        return answer
