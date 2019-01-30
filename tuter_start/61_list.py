# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k <= 0:
            return head
        num = 1
        tmp = head
        while tmp.next:
            num += 1
            tmp = tmp.next
        tmp.next = head
        k = k % num
        if k == num:
            return head
        k = num - k + 1
        tmp = head
        for i in range(k - 2):
            tmp = tmp.next
        new_head = tmp.next
        tmp.next = None

        return new_head

solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
result = solution.rotateRight(head, 2)
while result:
    print(result.val)
    result = result.next
