class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """最长回文子串
        暴力法O(N^3)
        """
        result = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]) and j-i+1 > len(result):
                    result = s[i:j+1]

        return result

    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def longestPalindrome_2(self, s):
        """
        动态规划 dp[i,j] = True dp[i+1, j-1] and s[i] == s[j]
        """
        """
        依次获得长度为1,2,3...的子串
        """
        if len(s) <= 1:
            return s
        dp = {}
        result = s[0]
        for i in range(0, len(s)):
            dp[(i, i)] = 1
            if i+1 < len(s) and s[i+1] == s[i]:
                dp[(i, i+1)] = 1
                if len(result) < 2:
                    result = s[i:i+2]
            else:
                dp[(i, i + 1)] = 0
        for s_len in range(3, len(s)+1):
            for start in range(len(s)-s_len+1):
                end = start + s_len - 1
                if start + 1 <= end - 1 and dp.get((start+1, end-1), None) == 1 and s[start] == s[end]:
                    dp[(start, end)] = 1
                    if len(result) < end - start + 1:
                        result = s[start: end+1]
                else:
                    dp[(start, end)] = 0

        return result

    def longestPalindrome_3(self, s):
        """
        """
        """中心扩展法
        把每个s[i]当作中心向两边扩展，把s[i,i+1]当作中心向两边扩展
        """
        if len(s) <= 1:
            return s
        result = ""
        for i in range(len(s)):
            ### s[i]是中心词
            j = i - 1
            k = i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                result = s[j:k+1] if len(result) < k - j + 1 else result
                j -= 1
                k += 1

        for i in range(len(s)):
            j = i
            k = i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                result = s[j:k + 1] if len(result) < k - j + 1 else result
                j -= 1
                k += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome_3("nn"))