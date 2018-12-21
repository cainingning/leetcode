# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    """完美二叉树，每一层节点数是一定的"""
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
    """start 标记每一层起始节点，cur用来遍历这一层"""
    def conncet_nb(self, root):
        if root is None:
            return
        start = root
        while start.left:
            current = start
            while current:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            start = start.elft

if __name__ == '__main__':
    solution = Solution()
    head = TreeLinkNode()
