# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        l = []
        def find_element(tree):

            if tree is None:
                return

            l.append(tree.val)

            if tree.left:
                find_element(tree.left)

            if tree.right:
                find_element(tree.right)

        def find_two_element():

            for x in range(len(l)-1):
                for y in l[x+1:]:
                    if l[x]+y == k:
                        return True
            return False

        find_element(root)
        return find_two_element()

