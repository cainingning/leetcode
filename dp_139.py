class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """回溯法
        容易超时
        s[0:index]是单词，再判断s[index+1:]能否分割
        """
        return self.wordBreak_bt(s, wordDict, 0)

    def wordBreak_bt(self, s, wordDict, start):
        if start == len(s):
            return True
        for i in range(start+1, len(s)+1):
            sub = s[start:i]
            if sub in wordDict and self.wordBreak_bt(s, wordDict, i):
                return True
        return False

    def wordBreak_dp(self, s, wordDict):
        if len(s) <= 0 or wordDict is None:
            return False
        """dp[i]表示s[:i]是否返回True
           dp[i]为true当dp[j]为true且s[i:j]在字典里
        """
        dp = [0] * len(s)
        for i in range(len(s)):
            for item in wordDict:
                j = len(item)
                if i+1 >= j and i + 1 <= len(s) and s[i+1-j:i+1] == item and (i+1-j == 0 or dp[i-j] == 1):
                    # print(i, j)
                    dp[i] = 1
                    break
        # print(dp)
        return dp[-1] == 1

if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak_dp("aaaaaaa" , ["aaaa","aaa"]))