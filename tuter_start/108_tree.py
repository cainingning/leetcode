# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        """一个分治的思想"""
        if len(nums) <= 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid_i = (0 + len(nums) - 1) // 2
        root = TreeNode(nums[mid_i])
        root.left = self.sortedArrayToBST(nums[:mid_i])
        root.right = self.sortedArrayToBST(nums[mid_i + 1:])

        return root

