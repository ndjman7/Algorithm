# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def find_all_tree(node):
            if node is None:
                return

            is_delete = True

            if node.left:
                left_delete = find_all_tree(node.left)
                if left_delete is True:
                    node.left = None
                else:
                    is_delete = False

            if node.right:
                right_delete = find_all_tree(node.right)
                if right_delete is True:
                    node.right = None
                else:
                    is_delete= False

            if node.val == 1:
                is_delete = False

            return is_delete

        find_all_tree(root)

        return root
