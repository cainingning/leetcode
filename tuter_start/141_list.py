# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        quick = head.next.next
        slow = head.next
        while quick and slow:
            if quick == slow:
                return True
            if quick.next is None:
                return False
            quick = quick.next.next
            slow = slow.next

        return False

    def hasCycle_better(self, head):
        if head is None or head.next is None:
            return False
        quick = head.next
        slow = head
        while slow != quick:
            if quick is None or quick.next is None:
                return False
            quick = quick.next.next
            slow = slow.next

        return True