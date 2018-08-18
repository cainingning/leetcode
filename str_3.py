class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        不包含重复字符的最长子串
        """
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        max_len = 0
        idx = -1 # 记录上一次出现的位置.如果没有出现重复字符就不更新
        pos_map = {}
        for i in range(len(s)):
            if pos_map.get(s[i]) is not None and pos_map.get(s[i]) > idx:
                idx = pos_map.get(s[i])
            if (i - idx) > max_len:
                max_len = i - idx

            pos_map[s[i]] = i

        return max_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    # if 'b' in 'b':
    #     print('not')
    # else:
    #     print('yes')
