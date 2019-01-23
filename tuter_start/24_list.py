# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """交换每两个链表节点的值"""
        if head is None or head.next is None:
            return head
        temp = head
        while temp and temp.next:
            temp.val, temp.next.val = temp.next.val, temp.val
            temp = temp.next.next

        return head
    def swapPairs_rec(self, head):
        """"""
        """如果节点是不能被改变，有两种办法。一种是递归，一种是非递归"""
        if head and head.next:
            """交换这两个节点"""
            tmp = head.next
            head.next = self.swapPairs_rec(tmp.next)
            tmp.next = head
            return tmp

        return head

    def swapPairs_nonrec(self, head):
        p = ListNode(-1)
        dummy = p
        dummy.next = head
        while head and head.next:
            """指向第二个节点"""
            tmp = head.next
            """第一个节点指向第三个节点"""
            head.next = tmp.next
            """p代表这两个节点的前一个节点。所以下一次要指导这两个中的第二个节点"""
            tmp.next = head
            p.next = tmp
            head = head.next
            p = tmp.next

        return dummy.next



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
result = Solution().swapPairs_nonrec(head)
while result:
    print(result.val)
    result = result.next

