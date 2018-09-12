# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        self.pathSum_recv(root, result, [], sum)

        return result
    ####递归算法
    def pathSum_recv(self, root, result, temp, sum):
        if root.left is None and root.right is None and root.val == sum:
            temp.append(root.val)
            result.append(temp)
        if root.left:
            self.pathSum_recv(root.left, result, temp + [root.val], sum - root.val)
        if root.right:
            self.pathSum_recv(root.right, result, temp + [root.val], sum - root.val)
    ###深度优先遍历，用先进先出的queue
    def pathSum_dfs(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        queue = [(root, [root.val])]
        while len(queue) > 0:
            current_node, temp = queue.pop(0)
            if current_node.left is None and current_node.right is None and sum(temp) == s:
                result.append(temp)
            if current_node.left:
                queue.append((current_node.left, temp + [current_node.left.val]))
            if current_node.right:
                queue.append((current_node.right, temp + [current_node.right.val]))

        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(-2)
    # root.left = TreeNode(4)
    root.right = TreeNode(-3)
    # root.left.right = TreeNode(11)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)

    print(solution.pathSum_dfs(root, -5))
