class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """数组中和为target的所有可能结果
        """
        result_list = []
        temp = []
        candidates.sort()
        self.findAllSolution(candidates, result_list, temp, target, 0)

        # print("result list ", result_list)
        return result_list

    def findAllSolution(self, candidates, result_list, temp, target, index):
        if target == 0:
            # print("find all result list", result_list)
            import copy
            result_list.append(copy.deepcopy(temp))
            # print("after find all result list", result_list)
            return
        else:
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    return
                temp.append(candidates[i])
                self.findAllSolution(candidates, result_list, temp, target - candidates[i], i)
                temp.pop()

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum( [2,3,5,6,7], 7))

