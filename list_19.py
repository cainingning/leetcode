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
        if head is None or n <= 0:
            return None
        forward = self.findNthFromEnd(head, n)
        pre_temp = head
        while pre_temp.next is not None and pre_temp.next != forward:
            pre_temp = pre_temp.next
        # print("pre_temp", pre_temp.val)
        if pre_temp.next is None:
            if forward is not None:
                return forward.next
            else:
                return None
        if forward.next is None:
            pre_temp.next = None
        else:
            pre_temp.next = forward.next

        return head

    def findNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or n <= 0:
            return None
        # set temp-pointer at n
        temp = head
        result = head
        for i in range(1, n):
            if temp.next is None:
                return None
            temp = temp.next
        while temp.next is not None:
            result = result.next
            temp = temp.next

        return result

if __name__ == '__main__':
    solution = Solution()
    temp = ListNode(1)
    temp.next = ListNode(2)
    # temp.next.next = ListNode(3)
    # temp.next.next.next = ListNode(4)

    result = solution.removeNthFromEnd(temp, 2)
    while result is not None:
        print(result.val)
        result = result.next