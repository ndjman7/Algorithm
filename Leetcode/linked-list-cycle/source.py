# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cycle = dict()
        while head != None:
            if id(head) not in cycle:
                cycle[id(head)] = True
                head = head.next
            else:
                return True
        return False
