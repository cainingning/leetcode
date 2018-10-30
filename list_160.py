# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        countA = 0
        tmpA = headA
        while tmpA is not None:
            tmpA = tmpA.next
            countA += 1
        countB = 0
        tmpB = headB
        while tmpB is not None:
            tmpB = tmpB.next
            countB += 1
        tmpA = headA
        tmpB = headB
        if countA > countB:
            for i in range(countA - countB):
                tmpA = tmpA.next
        else:
            for i in range(countB - countA):
                tmpB = tmpB.next
        while tmpA != tmpB and tmpA and tmpB:
            tmpA = tmpA.next
            tmpB = tmpB.next

        if tmpA == tmpB:
            return tmpA
        else:
            return None

if __name__ == '__main__':
    solution = Solution()
    head1 = ListNode(1)
    head2 = head1
    result = solution.getIntersectionNode(head1, head2)
    print(result)