class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        if len(x_str) <= 0:
            return True
        i = 0
        j = len(x_str) - 1
        while i < j:
            if x_str[i] != x_str[j]:
                return False
            i += 1
            j -= 1

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(10))