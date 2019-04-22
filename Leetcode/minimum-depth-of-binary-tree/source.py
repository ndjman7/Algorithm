# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    min_depth = 987654321
    def findDepth(self, node, cnt):
        if node.left:
            self.findDepth(node.left, cnt+1)
        if node.right:
            self.findDepth(node.right, cnt+1)
        if node.left is None and node.right is None:
            self.min_depth = min(self.min_depth, cnt)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.findDepth(root, 1)
            return self.min_depth
        else:
            return 0
