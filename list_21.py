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
        if l2 is None:
            return l1
        if l1 is None:
            return l2
        temp1 = l1
        temp2 = l2
        head = ListNode(-1)
        temp = head
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2

        return head.next

if __name__ == '__main__':
    head1 = ListNode(1)
    #head1.next = ListNode(3)
    #head1.next.next = ListNode(5)
    head2 = ListNode(2)
    # head2.next = ListNode(4)
    # head2.next.next = ListNode(6)

    solution = Solution()
    result = solution.mergeTwoLists(head1, head2)

    while result:
        print(result.val)
        result = result.next