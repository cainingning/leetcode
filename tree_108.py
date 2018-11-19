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
        if len(nums) == 0:
            return None

        return self.find_medium(nums, 0, len(nums) - 1)

    def find_medium(self, nums, l_index, r_index):
        if l_index > r_index:
            return None
        mid = int((l_index - r_index) / 2 + r_index)
        node = TreeNode(nums[mid])
        node.left = self.find_medium(nums, l_index, mid - 1)
        node.right = self.find_medium(nums, mid + 1, r_index)

        return node

