class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []
        map_store = {}
        for i in strs:
            k = str(sorted(list(i)))
            if map_store.get(k, None):
                map_store[k].append(i)
            else:
                map_store[k] = [i]
        res = []
        for k, v in map_store.items():
            res.append(v)

        return res

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

