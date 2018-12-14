class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0 or n <= 0:
            return 0

        result, tmp = [], []

        self.combine_bt(result, tmp, n, k, 1)

        return result



    def combine_bt(self, result, tmp, n, k, st_n):

        if len(tmp) == k:
            result.append(tmp.copy())
            return
        for i in range(st_n, n - (k - len(tmp)) + 1):
            tmp.append(i)
            self.combine_bt(result, tmp, n, k, i+1)
            tmp.pop(-1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(n = 4, k = 2))

