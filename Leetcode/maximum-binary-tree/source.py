# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def find_max_index(start, end):

            if start == end:
                return -1, -1
            max_index = -1
            max_value = -1
            for index in range(start, end):
                if max_value < nums[index]:
                    max_index = index
                    max_value = nums[index]
            return max_index, max_value

        def make_tree(node, start, end, max_index):
            if start == end:
                return

            max_left_index, max_left_value = find_max_index(start, max_index)
            if max_left_index != -1:
                left_node = TreeNode(max_left_value)
                node.left = left_node
                make_tree(node.left, start, max_index, max_left_index)

            max_right_index, max_right_value = find_max_index(max_index+1, end)
            if max_right_index != -1:
                right_node = TreeNode(max_right_value)
                node.right = right_node
                make_tree(node.right, max_index+1, end, max_right_index)

            return

        max_index, max_value = find_max_index(0, len(nums))
        root = TreeNode(max_value)

        make_tree(root, 0, len(nums), max_index)

        return root
