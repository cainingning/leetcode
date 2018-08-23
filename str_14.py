class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 0:
            return ""
        min_str = strs[0]
        for str in strs:
            if len(str) < len(min_str):
                min_str = str
        for i in range(len(min_str), 0, -1):
            sub_str = min_str[:i]
            count = 0
            for str in strs:
                if sub_str == str[:i]:
                    count += 1
                else:
                    break
            if count == len(strs):
                return sub_str

        return ""





if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["dog","racecar","car"]))
    print("sss"[:1])