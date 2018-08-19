class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        最长回文子串
        """
        if len(s) <= 0:
            return ""
        max_seq = s[0]
        for i in range(len(s)):
            sub_str = s[i:]
            for j in range(len(sub_str) - 1, -1, -1):
                if self.isPalindrome(sub_str[:j + 1]):
                    if len(max_seq) < len(sub_str[:j + 1]):
                        max_seq = sub_str[:j + 1]

        return max_seq

    def longestPalindrome_dp(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        p(i, j)=True当子串i-j是回文序列时。
        所以p(i, j) = True if p(i-1, j-1) and s[i] == s[j]
        """
        dp = [[False * len(s)] * len(s)]
        for i in range(len(s)):
            dp[i][1] = True
            dp[1][i] = True
        

    def isPalindrome(self, x_str):
        """
        :type x: str
        :rtype: bool
        """
        if len(x_str) <= 0:
            return True
        i = 0
        j = len(x_str) - 1
        while i < j:
            if x_str[i] != x_str[j]:
                return False
            i += 1
            j -= 1

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome( "cbbd"))

