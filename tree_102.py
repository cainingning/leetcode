# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        层次优先遍历就是深度优先遍历
        """
        if root is None:
            return [[]]
        result = {} # key 是层数，value是该层对应的节点数
        remain_node = [(root, 1)]
        while len(remain_node) > 0:
            now_tup = remain_node.pop(0)
            now_node = now_tup[0]
            now_layer = now_tup[1]
            if result.get(now_layer):
                result[now_layer].append(now_node.val)
            else:
                result[now_layer] = [now_node.val]
            if now_node.left is not None:
                remain_node.append((now_node.left, now_layer + 1))
            if now_node.right is not None:
                remain_node.append((now_node.right, now_layer + 1))
        sorted(result.items(), key=lambda  x: x[0])
        return_tmp = []
        for v in result.values():
            return_tmp.append(v)
        return return_tmp

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode()

