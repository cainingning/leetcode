# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        """time space trade off 可以不停的寻找链表的中点，然后一直递归构造最后的二叉树"""
        l = []
        while head:
            l.append(head.val)
            head= head.next

        return self.get_tree(l)

    def get_tree(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = (0 + len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.get_tree(nums[: mid])
        root.right = self.get_tree(nums[mid + 1:])

        return root
