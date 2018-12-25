# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        outer_p = head
        while outer_p:
            inner_p = outer_p
            while inner_p.next:
                i_v = inner_p.next.val
                o_v = outer_p.val
                if i_v < o_v:
                    outer_p.val = i_v
                    inner_p.next.val = o_v
                inner_p = inner_p.next
            outer_p = outer_p.next


        return head

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    result = solution.insertionSortList(head)
    while result:
        print(result.val)
        result = result.next
