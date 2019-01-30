class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if len(digits) == 0:
            return []
        digits = [str(x) for x in digits]
        num = int(str("".join(digits)))
        num += 1

        res = list(str(num))
        res = [int(x) for x in res]
        return res

solution = Solution()
print(solution.plusOne([9]))