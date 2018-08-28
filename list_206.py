# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        temp1 = head
        new_head = None
        while temp1 is not None:
            temp2 = temp1.next # 暂时保存temp1的笑一个节点的地址，防止丢失
            temp1.next = new_head
            new_head = temp1
            temp1 = temp2

        return new_head

if __name__ == '__main__':
    solution = Solution()
    temp = ListNode(1)
    # temp.next = ListNode(2)
    # temp.next.next = ListNode(3)

    result = solution.reverseList(temp)

    while result is not None:
        print(result.val)
        result = result.next