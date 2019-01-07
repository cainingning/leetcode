class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        """回溯是一种深度优先遍历，相当于从根节点出发遍历每个节点，符合条件继续往深度遍历，否则抛弃这条路径
        保存解的数组一直在动态改变，不用搞返回数据"""
        """可以用递归或者迭代来实现"""
        if len(digits) <= 0:
            return []
        res = []
        self.core(digits, res, '', 0)
        return res

    def core(self, digits, res, now_str, index):
        d = {'1':'', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if index >= len(digits):
            res.append(now_str)
            return
        chars = d.get(digits[index])
        for i in range(len(chars)):
            now_str += chars[i]
            self.core(digits, res, now_str, index + 1)
            now_str = now_str[:-1]

        return

solution = Solution()
print(solution.letterCombinations("23"))
