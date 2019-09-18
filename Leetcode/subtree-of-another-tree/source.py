# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        if t is None:
            return True

        answer = False
        sub_tree_root_val = t.val

        def check_sub_tree(l_tree, r_tree):

            if l_tree.val != r_tree.val:
                return False

            if l_tree.left is None and r_tree.left:
                return False

            if l_tree.left and r_tree.left is None:
                return False

            if l_tree.left and r_tree.left:
                val = check_sub_tree(l_tree.left, r_tree.left)
                if val is False:
                    return val


            if l_tree.right is None and r_tree.right:
                return False

            if l_tree.right and r_tree.right is None:
                return False

            if l_tree.right and r_tree.right:
                val = check_sub_tree(l_tree.right, r_tree.right)
                if val is False:
                    return val

            return True


        def find_sub_tree(tree):
            nonlocal t

            if tree is None:
                return

            if tree.val == sub_tree_root_val:
                if check_sub_tree(tree, t):
                    nonlocal answer
                    answer = True
                    return

            if tree.left:
                find_sub_tree(tree.left)

            if tree.right:
                find_sub_tree(tree.right)

        find_sub_tree(s)

        return answer

