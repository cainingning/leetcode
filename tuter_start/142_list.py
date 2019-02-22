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
        """S O(N)"""
        if head is None or head.next is None:
            return None
        tmp = []
        while head:
            if head in tmp:
                return head
            else:
                tmp.append(head)
            head = head.next

        return None

    def detectCycle_better(self, head):
        """"""
        """原点到入环点x1，入环点到相遇点x2，相遇点再回到入环点x3。
        快慢指针速度之比是2:1。
        2(x1+x2) = (x1+x2+x3+x2)
        所以x1=x3
        从原点和相遇点同时出发，此时的相遇点就是入环点
        """
        if head is None or head.next is None:
            return None
        slow = head.next
        quick = head.next.next
        while slow != quick:
            if quick is None or quick.next is None:
                return None
            quick = quick.next.next
            slow = slow.next
        tmp = head
        while tmp != slow:
            slow = slow.next
            tmp = tmp.next

        return tmp

