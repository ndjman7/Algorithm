# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def change_10bit(data):
            return_value = 0
            for index, value in enumerate(reversed(data)):
                if value == 1:
                    return_value += 2 ** index
            return return_value

        answer = 0
        bits = list()

        def make_2bits(node):

            bits.append(node.val)

            if node.left is None and node.right is None:
                nonlocal answer
                change_bit = change_10bit(bits)
                answer += change_bit
            if node.left:
                make_2bits(node.left)
            if node.right:
                make_2bits(node.right)

            bits.pop()

        make_2bits(root)
        return answer
