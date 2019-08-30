# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        ret = 0
        node = root
        def find_path(node, val):

            nonlocal ret

            if val + node.val == sum:
                ret += 1

            if node.left:
                find_path(node.left, val+node.val)

            if node.right:
                find_path(node.right, val+node.val)

            return

        def inorder(node):

            find_path(node, 0)

            if node.left:
                inorder(node.left)
            if node.right:
                inorder(node.right)

        if node:
            inorder(node)

        return ret
