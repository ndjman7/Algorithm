# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        new_node = TreeNode(val)

        def insert_val(node, new_node):
            if node is None:
                return

            if node.val < new_node.val:

                if node.right:
                    insert_val(node.right, new_node)

                else:
                    node.right = new_node
                    return

            if node.val > new_node.val:

                if node.left:
                    insert_val(node.left, new_node)

                else:
                    node.left = new_node
                    return

        insert_val(root, new_node)
        return root
