# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        tmp = head
        while tmp:
            res.append(tmp.val)
            tmp = tmp.next
        res = self.quick_sort(res, 0, len(res) - 1)
        tmp = head
        i = 0
        while tmp:
            tmp.val = res[i]
            i += 1
            tmp = tmp.next

        return head

    def quick_sort(self, nums, start, end):
        if start > end:
            return []
        i = start
        j = end
        pivot = nums[start]
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        self.quick_sort(nums, start, i - 1)
        self.quick_sort(nums, i + 1, end)

        return nums


solution = Solution()
l = [4, 2, 1, 3]
dumpy = ListNode(-1)
tmp = dumpy
for i in l:
    tmp.next = ListNode(i)
    tmp = tmp.next

tt= solution.sortList(dumpy)
while tt:
    print(tt.val)
    tt = tt.next
