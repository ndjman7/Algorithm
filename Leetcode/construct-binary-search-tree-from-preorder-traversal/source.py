# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        root = TreeNode(preorder[0])
        preorder = preorder[1:]

        def construct_tree(node, value):

            if node.val < value:
                if node.right is None:
                    new_node = TreeNode(value)
                    node.right = new_node

                else:
                    construct_tree(node.right, value)

            else:
                if node.left is None:
                    new_node = TreeNode(value)
                    node.left = new_node
                else:
                    construct_tree(node.left, value)

        for value in preorder:
            construct_tree(root, value)

        return root
