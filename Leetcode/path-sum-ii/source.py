# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        answer = []
        def find_all_path(node, path, value):

            path.append(node.val)

            if node.left:
                find_all_path(node.left, path[:], node.val+value)

            if node.right:
                find_all_path(node.right, path[:], node.val+value)

            if node.left is None and node.right is None:

                if node.val + value == sum:
                    answer.append(path)

            return

        if root:
            find_all_path(root, [], 0)

        return answer

