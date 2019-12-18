class Solution:
    def removeDuplicates(self, S: str) -> str:

        stack = []
        for s in S:
            if not stack or s != stack[-1]:
                stack += [s]
            else:
                stack.pop()
        return ''.join(stack)
