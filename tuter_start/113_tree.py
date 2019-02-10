# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.my_dfs(res, [], sum, root)

        return res

    def my_dfs(self, res, tmp, sum, node):
        if node is None:
            return
        if node.left is None and node.right is None and sum == node.val:
            tmp.append(node.val)
            import copy
            res.append(copy.copy(tmp))
            return
        # if sum < 0:
        #     return
        self.my_dfs(res, tmp + [node.val], sum - node.val, node.left)
        self.my_dfs(res, tmp + [node.val], sum - node.val, node.right)


solution = Solution()
root = TreeNode(-2)
# root.left = TreeNode(4)
root.right = TreeNode(-3)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(1)
print(solution.pathSum(root, -5))