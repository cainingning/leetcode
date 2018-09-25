class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        char_hash = {}
        for i in s:
            char_hash[i] = char_hash.get(i, 0) + 1
        sorted_map = sorted(char_hash.items(), key=lambda x: x[1], reverse=True)
        result = ''
        for k, v in sorted_map:
            # print(k, v)
            for i in range(v):
                result += k


        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.frequencySort("aabcc"))
