# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        def remove_node(node, target):

            if node is None:
                return

            if node.left:
                is_delete = remove_node(node.left, target)
                if is_delete:
                    node.left = None

            if node.right:
                is_delete = remove_node(node.right, target)
                if is_delete:
                    node.right = None

            # leaf node
            if node.left is None and node.right is None:
                if node.val == target:
                    return True

            return

        is_delete = remove_node(root, target)
        if is_delete:
            root = None

        return root

