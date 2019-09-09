def convertBST(self, root):
    def f(node, n):
        if node is None:
            return 0
        r = f(node.right, n)
        v = node.val
        node.val += (r + n)
        l = f(node.left, node.val)
        return r + l + v

    f(root, 0)

    return root
