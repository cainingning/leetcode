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
        所以p(i, j) = True if p(i+1, j-1) and s[i] == s[j]
        dp只维护右上三角矩阵
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        # print(dp)
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
        # print(dp)
        # 一字符串和二字符串的已经计算完了
        for char_count in range(2, len(s)):
            for i in range(len(s)):
                j = i + char_count
                if j < len(s) and dp[i + 1][j - 1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
        # print(dp)
        max_seq = s[0]
        for i in range(len(dp)):
            for j in range(len(dp)):
                if dp[i][j] == 1 and (j - i + 1) > len(max_seq):
                    max_seq = s[i: j + 1]

        return max_seq

    def longestPalindrome_simple(self, s):
        """
        以每个字符,或者是字符的间隙作为中间字符像左右扩展找最长回文子串
        :param s:
        :return:
        """
        if len(s) <= 0:
            return ""
        max_seq = s[0]
        for i in range(2 * len(s) - 1):
            left_index = int(i / 2)
            right_index = int(i / 2)
            if i % 2 == 1:
                right_index += 1
            while left_index >= 0 and right_index < len(s):
                if s[left_index] != s[right_index]:
                    break
                left_index -= 1
                right_index += 1
            left_index += 1
            right_index -= 1
            if right_index - left_index + 1 > len(max_seq):
                max_seq = s[left_index: right_index + 1]

        return max_seq


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
    # print(solution.longestPalindrome( "cbbd"))
    # print(solution.longestPalindrome_dp("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
    # print(solution.longestPalindrome_dp("abcba"))
    test_str = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    print(solution.longestPalindrome_simple(test_str))
    print(solution.longestPalindrome_simple("cbbd"))
