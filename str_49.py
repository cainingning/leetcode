class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """key是字母.value是其对应的list"""
        dict_tmp = {}
        for item in strs:
            l_item = sorted(list(item))
            now_key = ''.join(l_item)
            if dict_tmp.get(now_key, 0) == 0:
                dict_tmp[now_key] = [item]
            else:
                dict_tmp[now_key].append(item)

        result = []
        for k, v in dict_tmp.items():
            print(k, v)
            result.append(v)

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))
