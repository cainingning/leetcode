# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow = head
        fast = head
        while True:
            slow = slow.next
            fast = fast.next.next
            if slow is None or fast is None:
                return None
            if slow == fast:
                break
        temp1 = head
        temp2 = slow
        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next

        return temp1
