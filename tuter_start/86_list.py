# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = []
        more = []
        tmp = head
        while tmp:
            if tmp.val < x:
                less.append(tmp.val)
            else:
                more.append(tmp.val)
            tmp = tmp.next
        tmp = head
        for i in less + more:
            tmp.val = i
            tmp = tmp.next

        return head
    def partition_2(self, head, x):
        """"""
        """less, more指针为头构造两条链表，再把两条链表连接起来"""
        """比上面的算法时间短"""
        less = ListNode(-1)
        more = ListNode(-1)
        tmp, tmp_less, tmp_more = head, less, more
        while tmp:
            if tmp.val < x:
                tmp_less.next = tmp
                tmp_less = tmp_less.next
            else:
                tmp_more.next = tmp
                tmp_more = tmp_more.next
            tmp = tmp.next
        tmp_more.next = None
        tmp_less.next = more.next

        return less.next



solution = Solution()
head = ListNode(1)
tmp = head
for i in [4, 3, 2, 5, 2]:
    tmp.next = ListNode(i)
    tmp = tmp.next
result = solution.partition_2(head, 3)
while result:
    print(result.val)
    result = result.next


