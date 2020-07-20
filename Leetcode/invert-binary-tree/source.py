# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):

        if not root:
            return
        if root.left or root.right:
            l=root.left
            r=root.right
            root.left=r
            root.right=l
            self.helper(root.left)
            self.helper(root.right)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return
        return self.helper(root)
