# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        answer = 0

        def find_path_sum(node, val):

            nonlocal answer

            if node.left:
                find_path_sum(node.left, val+node.val)

            if node.right:
                find_path_sum(node.right, val+node.val)

            if node.left is None and node.right is None:
                if node.val + val == sum:
                    answer += 1

            return
        if root:
            find_path_sum(root, 0)
        return answer
