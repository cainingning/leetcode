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
        new_head = head
        while head is not None:
            tmp = head.next
            if tmp and head.val == tmp.val:
                if tmp.next is not None:
                    head.next = tmp.next
                else:
                    head.next = None
                    break
            else:
                head = head.next

        return new_head

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    l = [1, 2, 3, 3, 4]
    tmp = head
    for i in l:
        tmp.next = ListNode(i)
        tmp = tmp.next
    new_head = solution.deleteDuplicates(head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next