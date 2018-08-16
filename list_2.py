# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        result = ListNode(0)
        temp1 = l1
        temp2 = l2
        temp = result
        move = 0
        while temp1 and temp2:
            current_num = temp1.val + temp2.val + move
            if current_num >= 10:
                temp.next = ListNode(current_num - 10)
                move = 1
            else:
                temp.next = ListNode(current_num)
                move = 0
            temp = temp.next
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1:
            current_num = temp1.val + move
            if current_num >= 10:
                temp.next = ListNode(current_num - 10)
                move = 1
            else:
                temp.next = ListNode(current_num)
                move = 0
            temp = temp.next
            temp1 = temp1.next
        while temp2:
            current_num = temp2.val + move
            if current_num >= 10:
                temp.next = ListNode(current_num - 10)
                move = 1
            else:
                temp.next = ListNode(current_num)
                move = 0
            temp = temp.next
            temp2 = temp2.next
        if move == 1:
            temp.next = ListNode(1)

        return result.next

if __name__ == '__main__':
    solution = Solution()
    list1 = ListNode(5)
    # list1.next = ListNode(9)
    # list1.next.next = ListNode(3)
    list2 = ListNode(5)
    # list2.next = ListNode(2)
    # list2.next.next = ListNode(3)
    result = solution.addTwoNumbers(list1, list2)
    while result:
        print(result.val)
        result = result.next