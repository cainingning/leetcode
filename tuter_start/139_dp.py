class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """dp的状态转移方程
        dp[i] is true if dp[j] is true and s[j+1:i+1] in wordDict"""
        if len(s) == 0 or wordDict is None:
            return False
        dp = [False] * len(s)
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                dp[i] = True
                continue
            for j in range(i):
                if dp[j] and s[j + 1:i + 1] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]

    def wordBreak_better(self, s, wordDict):
        if len(s) == 0 or wordDict is None:
            return False
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1: i + 1] and (dp[i - len(w)] or i - len(w) == -1):
                    dp[i] = True

        return dp[-1]

solution = Solution()
print(solution.wordBreak_better(s = "leetcode", wordDict = ["leet", "code"]))
