# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        """tmp2指向下一个和tmp1不一样的节点"""
        if head is None or head.next is None:
            return head
        tmp1 = head
        tmp2 = head
        while tmp2:
            while tmp1 and tmp2 and tmp1.val == tmp2.val:
                tmp2 = tmp2.next
            tmp1.next = tmp2
            tmp1 = tmp2

        return head

solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(3)

result = solution.deleteDuplicates(head)
while result:
    print(result.val)
    result = result.next
