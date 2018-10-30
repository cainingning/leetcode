class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_map = {}
        for i in nums:
            if hash_map.get(i, None) is None:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        for k, v in hash_map.items():
            if v >= 2:
                return True

        return False

