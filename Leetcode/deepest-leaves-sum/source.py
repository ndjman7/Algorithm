# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        data = {}
        max_level = 0
        def find_data(node, level):
            if node is None:
                return

            nonlocal max_level
            max_level = max(max_level, level)
            if data.get(level):
                data[level].append(node.val)
            else:
                data[level] = [node.val]

            if node.left:
                find_data(node.left, level+1)

            if node.right:
                find_data(node.right, level+1)

            return

        find_data(root, 1)
        return sum(data[max_level])
