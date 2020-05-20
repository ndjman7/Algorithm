# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0
        def find_good_node(node, max_value):
            nonlocal answer
            if node is None:
                return

            if node.val >= max_value:
                answer += 1

            max_value = max(max_value, node.val)
            find_good_node(node.left, max_value)
            find_good_node(node.right, max_value)

        find_good_node(root, root.val)

        return answer
