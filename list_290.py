class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p_l = list(pattern)
        s_l = str.strip().split(" ")
        if len(p_l) != len(s_l) or p_l == 0 or s_l == 0:
            return False
        temp_dict_1 = {}
        temp_dict_2 = {}
        for i in range(len(p_l)):
            if temp_dict_1.get(s_l[i], 0) == 0:
                temp_dict_1[s_l[i]] = p_l[i]
            if temp_dict_2.get(p_l[i], 0) == 0:
                temp_dict_2[p_l[i]] = s_l[i]
            cmp_str = temp_dict_1[s_l[i]]
            if cmp_str != p_l[i]:
                return False
            cmp_str = temp_dict_2[p_l[i]]
            if cmp_str != s_l[i]:
                return False

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.wordPattern(  pattern = "abba", str = "dog cat cat dog"))