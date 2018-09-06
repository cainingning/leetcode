# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        设置两个指针，一个一次走1步，一个一次走两步，如果相遇有环。中间断了说明没环
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

if __name__ == '__main__':
    solution = Solution()
    test = ListNode(1)
    test.next = ListNode(2)
    test.next.next = ListNode(3)
    # test.next.next.next = test

    print(solution.hasCycle(test))
