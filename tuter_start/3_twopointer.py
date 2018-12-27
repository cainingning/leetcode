class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        暴力法
        time O(N^3)
        space O(1)
        """
        max_len = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if self.isUnique(s[i:j]):
                    max_len = max(max_len, j-i)

        return max_len

    def isUnique(self, str):
        for i in range(len(str)):
            if str[i] in str[i+1:]:
                return False

        return True

    def lengthOfLongestSubstring_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        滑窗法：对于每一个字符，检查以它为起始的最长的无重复子串有多长。
        定义字符到索引的映射map,而不是使用set保存检查的子串
        time O(N)
        space O(n))
        """
        if len(s) <= 1:
            return len(s)
        store_map = {}
        start, end = 0, 0
        result = 0
        while end < len(s):
            if store_map.get(s[end], None) is not None:
                start = max(start, store_map[s[end]])
            result = max(result, end-start+1)
            store_map[s[end]] = end+1
            end += 1

        return result
    def lengthOfLongestSubstring_3(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        滑窗i,j保存[i, j)的字符在一个set中
        s[j] in set:j+=1
        not in set:s[i]移出set, i+=1
        time:O(N)
        space:O(N)
        
        """
        if len(s) <= 1:
            return len(s)
        i, j = 0, 0
        tmp_set = set()
        result = 0
        while i < len(s) and j < len(s):
            if s[j] not in tmp_set:
                tmp_set.add(s[j])
                result = max(result, j-i+1)
                j += 1
            else:
                tmp_set.remove(s[i])
                i += 1
        return result



if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring_2("pwwkew"))