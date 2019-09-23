# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        hash_set = set()

        def find(root):
            if root is None:
                return False
            if k - root.val in hash_set:
                return True
            hash_set.add(root.val)
            return find(root.left) or find(root.right)

        return find(root)
