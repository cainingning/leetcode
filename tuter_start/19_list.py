# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """删除链表的倒数第k个元素"""
        if head is None or n <= 0:
            return None
        temp1, temp2 = head, head
        for i in range(n):
            temp1 = temp1.next
        if temp1 is None:
            return head.next
        while temp1.next:
            temp1 = temp1.next
            temp2 = temp2.next
        temp2.next = temp2.next.next

        return head

solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = solution.removeNthFromEnd(head, 1)
while result:
    print(result.val)
    result = result.next

