class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0:
            return -1
        m = {}
        for i in range(len(s)):
            if m.get(s[i], 0) == 0:
                m[s[i]] = [i, 1]
            else:
                m[s[i]][-1] += 1
        minIndex = len(s)
        for k, v in m.items():
            if v[1] == 1 and v[0] < minIndex:
                minIndex = v[0]
        if minIndex == len(s):
            return -1
        else:
            return minIndex
if __name__ == '__main__':
    solution = Solution()
    print(solution.firstUniqChar(s = "loveleetcode"))


