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
        if root is None:
            return root
        tmp = [[root, 0]]
        while len(tmp) > 0:
            node, layer = tmp.pop(0)
            if node.left:
                tmp.append([node.left, layer + 1])
            if node.right:
                tmp.append([node.right, layer + 1])
            if len(tmp) > 0 and tmp[0][1] == layer:
                node.next = tmp[0][0]
        return root