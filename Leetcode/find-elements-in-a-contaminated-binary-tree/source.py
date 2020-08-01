# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        self.cache = []
        self.cache.append(0)

        def set_val(node):

            if node.left:
                node.left.val = 2 * node.val + 1
                self.cache.append(node.left.val)
                set_val(node.left)

            if node.right:
                node.right.val = 2 * node.val + 2
                self.cache.append(node.right.val)
                set_val(node.right)

        set_val(self.root)

    def find(self, target: int) -> bool:

        if target in self.cache:
            return True
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
