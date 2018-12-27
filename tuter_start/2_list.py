# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        new_head = ListNode(-1)
        p, q, tmp = l1, l2, new_head
        add = 0
        while p and q:
            if p.val + q.val + add >= 10:
                tmp.next = ListNode(p.val+q.val+add-10)
                add = 1
            else:
                tmp.next = ListNode(p.val+q.val+add)
                add = 0
            tmp = tmp.next
            p = p.next
            q = q.next
        if q is not None:
            p = q
        while p:
            if p.val + add >= 10:
                tmp.next = ListNode(p.val+add-10)
                add = 1
            else:
                tmp.next = ListNode(p.val+add)
                add = 0
            tmp = tmp.next
            p = p.next
        if add == 1:
            tmp.next = ListNode(1)
        return new_head.next

    def addTwoNumbers_2(self, l1, l2):
        """

        :param l1:
        :param l2:
        :return:
        """
        """写法好优美"""
        add, now_sum = 0, 0
        p, q = l1, l2
        new_head = ListNode(-1)
        tmp = new_head
        while p or q or add:
            now_sum = add + (p.val if p else 0) + (q.val if q else 0)
            add = 1 if now_sum > 9 else 0
            tmp.next = ListNode(now_sum%10)
            tmp = tmp.next
            if p:
                p = p.next
            if q:
                q = q.next

        return new_head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    result = Solution().addTwoNumbers_2(l1, l2)
    while result:
        print(result.val)
        result = result.next
