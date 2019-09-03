# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def is_same_tree(p_node, q_node):

            if p_node.val != q_node.val:
                return False

            if p_node.left and q_node.left is None:
                return False

            if p_node.left is None and q_node.left:
                return False

            if p_node.left and q_node.left:
                progress = is_same_tree(p_node.left, q_node.left)
                if not progress:
                    return False

            if p_node.right and q_node.right is None:
                return False

            if p_node.right is None and q_node.right:
                return False

            if p_node.right and q_node.right:
                progress = is_same_tree(p_node.right, q_node.right)
                if not progress:
                    return False

            return True

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        return is_same_tree(p, q)
