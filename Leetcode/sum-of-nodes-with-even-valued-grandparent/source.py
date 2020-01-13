# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        answer = 0

        def sum_even_valued_grandparent(grandparent, parent, node):
            if node is None:
                return

            if grandparent:
                if grandparent % 2 == 0:
                    nonlocal answer
                    answer += node.val

            if node.left:
                sum_even_valued_grandparent(parent, node.val, node.left)

            if node.right:
                sum_even_valued_grandparent(parent, node.val, node.right)

            return

        sum_even_valued_grandparent(None, None, root)

        return answer
