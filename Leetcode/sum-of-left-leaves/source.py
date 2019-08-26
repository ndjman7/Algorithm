# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
sum_value = 0

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        global sum_value
        sum_value = 0
        tree = root
        def in_order(parent, node):
            if node is None:
                return None
            global sum_value
            if node.left:
                in_order('left', node.left)
            if node.right:
                in_order('right', node.right)

            if parent == 'left' and node.left is None and node.right is None:
                sum_value += node.val

        in_order('root', tree)

        return sum_value

