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
        # TODO [1, 2] 2的输入时有 Bug
        if head is None or head.next is None or k <= 0:
            return head
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        new_k = k % length
        if new_k == 0:
            return head
        sub_tail = head
        for i in range(length - new_k - 1):
            sub_tail = sub_tail.next
        new_head = sub_tail.next
        sub_tail.next = None
        tail.next = head

        return new_head

if __name__ == "__main__":
    solution = Solution()
    test = ListNode(0)
    test.next = ListNode(1)
    # test.next.next = ListNode(2)
    result = solution.rotateRight(test, 2)
    while result is not None:
        print(result.val)
        result = result.next


