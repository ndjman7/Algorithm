# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf_nodes = []
        def order(node):
            if node.left:
                order(node.left)
            if node.right:
                order(node.right)
            if node.left is None and node.right is None:
                leaf_nodes.append(node.val)

        order(root1)
        leaf_root1 = leaf_nodes.copy()

        leaf_nodes = []
        order(root2)

        for node1, node2 in zip(leaf_root1, leaf_nodes):
            if node1 != node2:
                return False
        return True
