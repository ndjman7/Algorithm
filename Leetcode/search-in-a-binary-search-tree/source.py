# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        def find_val(node):
            if node is None:
                return None

            if node.val == val:
                return node

            if node.val > val:
                return find_val(node.left)

            if node.val < val:
                return find_val(node.right)

        return find_val(root)
