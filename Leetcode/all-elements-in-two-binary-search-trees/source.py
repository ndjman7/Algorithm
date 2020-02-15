# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        answer = []

        def find_node(node):
            if node is None:
                return

            if node.left:
                find_node(node.left)
            if node.right:
                find_node(node.right)

            answer.append(node.val)

        find_node(root1)
        find_node(root2)

        return sorted(answer)
