# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for num in preorder[1:]:
            cur_node = TreeNode(num)
            if stack[-1].val > num:
                stack[-1].left = cur_node
                stack.append(cur_node)
            else:
                while True:
                    prev_node = stack.pop()
                    if len(stack) == 0 or stack[-1].val > num:
                        break
                prev_node.right = cur_node
                stack.append(cur_node)

        return root
