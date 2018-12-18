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
        store_dup = []
        tmp = head
        while tmp:
            count = 1
            while tmp.next and tmp.next.val == tmp.val:
                count += 1
                tmp = tmp.next
            if count > 1:
                store_dup.extend([1] * count)
            else:
                store_dup.append(0)
            tmp = tmp.next
        tmp = ListNode(0)
        new_head = tmp
        for i in store_dup:
            if i == 0:
                tmp.next = ListNode(head.val)
                head = head.next
                tmp = tmp.next
            else:
                head = head.next

        return new_head.next


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
