# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None or (root.left is None and root.right is None):
            return
        tmp = [root]

        while len(tmp) > 0:
            num = len(tmp)
            for i in range(num):
                node = tmp.pop(0)
                if i < num - 1:
                    node.next = tmp[0]
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
