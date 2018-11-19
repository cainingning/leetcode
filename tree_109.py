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
        if head is None:
            return None

        to_list = []
        tmp = head
        while tmp:
            to_list.append(tmp.val)
            tmp = tmp.next

        return self.find_search_tree(to_list, 0, len(to_list) - 1)

    def find_search_tree(self, nums, l_index, r_index):
        if l_index > r_index:
            return None
        mid = int((l_index - r_index) / 2 + r_index)
        node = TreeNode(nums[mid])
        node.left = self.find_search_tree(nums, l_index, mid - 1)
        node.right = self.find_search_tree(nums, mid + 1, r_index)

        return node