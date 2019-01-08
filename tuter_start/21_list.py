# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        new_head = ListNode(-1)
        temp1, temp2, temp = l1, l2, new_head
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1 is None:
            temp1 = temp2
        while temp1:
            temp.next = temp1
            temp = temp.next
            temp1 = temp1.next

        return new_head.next

l1 = ListNode(1)
l1.next = ListNode(4)
l2 = ListNode(2)
l2.next = ListNode(3)

result = Solution().mergeTwoLists(l1, l2)
while result:
    print(result.val)
    result = result.next
