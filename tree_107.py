# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        深度优先遍历，同时记录层数:节点
        """
        if root is None:
            return []
        dfs = []
        dfs_store = []
        dfs_store.append((1, root))
        while len(dfs_store) > 0:
            parent_info = dfs_store.pop(0)
            parent_layer = parent_info[0]
            parent = parent_info[1]
            dfs.append((parent_layer, parent.val))
            if parent.left is not None:
                dfs_store.append((parent_layer + 1, parent.left))
            if parent.right is not None:
                dfs_store.append((parent_layer + 1, parent.right))

        """
        按照层数从高到低输出
        """
        dfs.sort(key=self.get_first, reverse=True)
        result = []
        pre_layer = dfs[0][0]
        temp = [dfs[0][1]]
        for i in range(1, len(dfs)):
            if dfs[i][0] != pre_layer:
                pre_layer = dfs[i][0]
                result.append(temp)
                temp = [dfs[i][1]]
            else:
                temp.append(dfs[i][1])

        result.append(temp)

        return result


    def get_first(self, element):
        return element[0]

    def levelOrderBottom2(self, root):
        """
                深度优先遍历，同时记录层数:节点
                """
        if root is None:
            return []
        result = []
        dfs_store = []
        dfs_store.append((1, root))
        while len(dfs_store) > 0:
            parent_info = dfs_store.pop(0)
            parent_layer = parent_info[0]
            parent = parent_info[1]
            if parent is not None:
                if len(result) < parent_layer:
                    result.insert(0, [])
                result[-(parent_layer)].append(parent.val)
            if parent.left is not None:
                dfs_store.append((parent_layer + 1, parent.left))
            if parent.right is not None:
                dfs_store.append((parent_layer + 1, parent.right))

        return result

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print(solution.levelOrderBottom2(root))
