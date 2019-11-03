# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def bst_to_gst(node, value):

            if node is None:
                return value

            if node.right:
                value = bst_to_gst(node.right, value)

            value += node.val
            node.val = value

            if node.left:
                value = bst_to_gst(node.left, value)

            return value

        bst_to_gst(root, 0)

        return root
