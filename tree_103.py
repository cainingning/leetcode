# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        layer_node_map = {}
        temp = [(1, root)]
        while len(temp) > 0 :
            pop_node = temp.pop(0)
            layer = pop_node[0]
            node = pop_node[1]
            if layer_node_map.get(layer, 0) == 0:
                layer_node_map[layer] = [node.val]
            else:
                layer_node_map[layer].append(node.val)
            if node.left:
                temp.append((layer + 1, node.left))
            if node.right:
                temp.append((layer + 1, node.right))

        result = []
        for k, v in layer_node_map.items():
            if k % 2 == 0:
                v.reverse()
            result.append(v)

        return result

if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    print(solution.zigzagLevelOrder(tree))