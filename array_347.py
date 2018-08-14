class Solution:
    def topKFrequent_extraSpace(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        word_count = {}
        for i in nums:
            word_count[i] = word_count.get(i, 0) + 1
        word_count = sorted(word_count.items(), key=lambda k: k[1], reverse=True)
        keys, _ = zip(*word_count)
        return list(keys[:k])

    def topKFrequent(self, nums, k):
        word_count = {}
        time_count = {}
        result = []
        for i in nums:
            word_count[i] = word_count.get(i, 0) + 1
        for key, v in word_count.items():
            if v in time_count:
                time_count[v].append(key)
            else:
                time_count[v] = [key]
        for x in range(len(nums), 0, -1):
            if x in time_count:
                for j in time_count[x]:
                    # print("j", j)
                    result.append(j)
        return result[:k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1,1,1,2,2,3], 2))