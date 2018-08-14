class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_list = []
        temp = []
        candidates.sort()
        self.findAllSolution(candidates, result_list, temp, target, 0)

        return result_list

    def findAllSolution(self, candidates, result_list, temp, target, index):
        if target == 0:
            result_list.append(temp)
            return
        else:
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    return
                temp.append(candidates[i])
                self.findAllSolution(candidates, result_list, temp, target - candidates[i], i)
                temp.pop(-1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum( [2,3,6,7], 7))

