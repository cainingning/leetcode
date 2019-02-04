# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """递归"""
        if root is None:
            return True
        return self.core(root.left, root.right)


    def core(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            return self.core(left.left, right.right) & self.core(left.right, right.left)
        else:
            return False

    def isSymmetric_2(self, root):
        """"""
        """非递归"""
        if root is None:
            return True
        q_queue = [root]
        q_queue.append(root)
        while len(q_queue) > 0:
            left = q_queue.pop(-1)
            right = q_queue.pop(-1)
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            q_queue.append(left.left)
            q_queue.append(right.right)
            q_queue.append(left.right)
            q_queue.append(right.left)

        return True
