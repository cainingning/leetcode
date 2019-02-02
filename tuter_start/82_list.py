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
        if head is None or head.next is None:
            return head
        new_head = ListNode(-1)
        new_head.next = head
        tmp1 = new_head
        tmp2= head
        while tmp2 and tmp2.next:
            if tmp2.val == tmp2.next.val:
                while tmp2 and tmp2.next and tmp2.val == tmp2.next.val:
                    tmp2 = tmp2.next
                tmp2 = tmp2.next
                tmp1.next = tmp2
            else:
                tmp1 = tmp1.next
                tmp2 = tmp2.next



        return new_head.next

solution = Solution()
ss = ListNode(1)
ss.next = ListNode(1)
ss.next.next = ListNode(1)
ss.next.next.next = ListNode(2)
ss.next.next.next.next = ListNode(3)

result = solution.deleteDuplicates(ss)
while result:
    print(result.val)
    result = result.next

