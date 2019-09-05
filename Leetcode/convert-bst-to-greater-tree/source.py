# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        node = root

        def get_greater_tree(node, value):

            l = r = 0
            v = node.val

            if node.right:
                r = get_greater_tree(node.right, value)

            node.val += (value + r)

            if node.left:
                l = get_greater_tree(node.left, node.val)

            return l + r + v

        if node:
            get_greater_tree(node, 0)

        return root
