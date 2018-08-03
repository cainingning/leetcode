class Solution:
    def isIdealPermutation_timeout(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        local_num = 0
        glob_num = 0
        for i in range(0, len(A) - 1):
            if A[i] > A[i + 1]:
                local_num += 1
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    glob_num += 1

        return local_num == glob_num

    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        """
        因为数字是在0---n-1的。所有的local-inverse都是glob-inverse，所以一旦一个位置比她上面的数差2以上，local永远追不上glob了
        """
        for i in range(len(A)):
            if abs(A[i] - i) >= 2:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIdealPermutation([1, 2, 0]))