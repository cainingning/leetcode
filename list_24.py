# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        pre = head
        now = head.next
        while pre and now:
            pre.val, now.val = now.val, pre.val
            pre = now.next
            if pre is None:
                break
            now = pre.next


        return head


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    temp = head
    for i in range(2, 7):
        temp.next = ListNode(i)
        temp = temp.next
    result = solution.swapPairs(head)
    while result:
        print(result.val)
        result = result.next
