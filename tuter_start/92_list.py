# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or m >= n:
            return head
        tmp = []
        tmp_node = head
        while tmp_node:
            tmp.append(tmp_node.val)
            tmp_node = tmp_node.next
        m = m - 1
        n = n - 1
        while m < n:
            tmp[m], tmp[n] = tmp[n], tmp[m]
            m += 1
            n -= 1
        tmp_node = head
        i = 0
        while tmp_node:
            tmp_node.val = tmp[i]
            tmp_node = tmp_node.next
            i += 1

        return head

solution = Solution()
root = ListNode(0)
tmp = root
for i in [1, 2, 3, 4, 5]:
    tmp.next = ListNode(i)
    tmp = tmp.next
result = solution.reverseBetween(root, 3, 5)
while result:
    print(result.val)
    result = result.next

