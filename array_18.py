class Solution:
    def fourSum_diff(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

    def fourSum(self, nums, target):
        if len(nums) <= 3 or target is None:
            return []
        sorted_nums = sorted(nums)
        result = []
        for index_1 in range(len(sorted_nums) - 3):
            if index_1 > 0 and sorted_nums[index_1] == sorted_nums[index_1 - 1]:
                continue
            for index_2 in range(index_1 + 1, len(sorted_nums) - 2):
                if index_2 > index_1 + 1 and sorted_nums[index_2] == sorted_nums[index_2 - 1]:
                    continue
                index_3 = index_2 + 1
                index_4 = len(sorted_nums) - 1
                while index_3 < index_4:
                    now_sum = sorted_nums[index_1] + sorted_nums[index_2] + sorted_nums[index_3] + \
                              sorted_nums[index_4]
                    if now_sum == target:
                        result.append([sorted_nums[index_1], sorted_nums[index_2], sorted_nums[index_3],
                                       sorted_nums[index_4]])
                        index_3 += 1
                        while index_3 < index_4 and sorted_nums[index_3] == sorted_nums[index_3 + 1]:
                            index_3 += 1
                        index_4 -= 1
                        while index_3 < index_4 and sorted_nums[index_4] == sorted_nums[index_4 - 1]:
                            index_4 -= 1
                    elif now_sum < target:
                        index_3 += 1
                        while index_3 < index_4 and sorted_nums[index_3] == sorted_nums[index_3 + 1]:
                            index_3 += 1
                    else:
                        index_4 -= 1
                        while index_3 < index_4 and sorted_nums[index_4] == sorted_nums[index_4 - 1]:
                            index_4 -= 1

        return result


    def fourSum_easy(self, nums, target):
        """用哈希表
        """
        if len(nums) <= 3 or target is None:
            return []
        result = set()
        tmp = {}
        l = len(nums)
        nums.sort()
        for i_1 in range(l):
            for i_2 in range(i_1 + 1, l):
                if tmp.get((nums[i_1] + nums[i_2]), 0) == 0:
                    tmp[(nums[i_1] + nums[i_2])] = [(i_1, i_2)]
                else:
                    tmp[(nums[i_1] + nums[i_2])].append([i_1, i_2])

        for i_3 in range(l):
            for i_4 in range(i_3 + 1, l):
                need = target - nums[i_3] - nums[i_4]
                if tmp.get(need, 0) == 0:
                    continue
                for k in tmp[need]:
                    # print(k[0], k[1])
                    if k[0] > i_4:
                        result.add((nums[i_3], nums[i_4], nums[k[0]], nums[k[1]]))

        return [list(i) for i in result]



if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum_easy([-3,-2,-1,0,0,1,2,3], 0))
