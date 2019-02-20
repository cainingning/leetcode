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
        """对list进行插入排序"""
        if head is None or head.next is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            """如果cur是一个逆序的数字"""
            if cur.next and cur.next.val < cur.val:
                """将cur.next插入pre的下一个节点"""
                while pre.next and pre.next.val < cur.next.val:
                    pre = pre.next
                tmp = pre.next
                pre.next = cur.next
                cur.next = cur.next.next
                """之前保留的pre的下一个节点没有丢"""
                pre.next.next = tmp
                """pre永远指向第一个节点。方便插入排序找插入位置"""
                pre = dummy
            else:
                cur = cur.next

        return dummy.next
