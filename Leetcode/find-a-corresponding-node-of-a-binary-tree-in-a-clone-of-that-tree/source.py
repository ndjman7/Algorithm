# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def find_clone_node(node):
            if node is None:
                return

            if node.val == target.val:
                return node

            lnode = find_clone_node(node.left)
            if lnode:
                return lnode

            rnode = find_clone_node(node.right)
            return rnode

        return find_clone_node(cloned)
