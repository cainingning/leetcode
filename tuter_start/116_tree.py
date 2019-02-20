# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        """这是一个非常完整的二叉树，每层的数目都是2**(n - 1)"""
        if root is None:
            return root
        layer_first = root
        cur = None
        while layer_first.left:
            cur = layer_first
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            layer_first = layer_first.left

        return root








