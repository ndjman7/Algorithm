# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        unival = root.val
        is_unival = True

        def find_not_univalued_node(node):

            if node is None:
                return

            if node.val != unival:
                nonlocal is_unival
                is_unival = False
                return False

            if node.left:
                find_not_univalued_node(node.left)

            if node.right:
                find_not_univalued_node(node.right)
            return

        find_not_univalued_node(root)

        return is_unival
