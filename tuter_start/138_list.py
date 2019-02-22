# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        """深度复制这个链表， 利用哈希表"""
        """point:[]取dict的值在遇到不存在的key时会抛出key error异常！，get()却不会哦"""
        if head is None:
            return head
        tmp_dict = {}
        tmp = head
        while tmp:
            tmp_dict[tmp] = RandomListNode(tmp.label)
            tmp = tmp.next
        tmp = head
        while tmp:
            tmp_dict[tmp].next = tmp_dict.get(tmp.next)
            tmp_dict[tmp].random = tmp_dict.get(tmp.random)
            tmp = tmp.next

        return tmp_dict.get(head)