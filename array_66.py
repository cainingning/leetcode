class Solution:
    def plusOne_test1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None or len(digits) == 0:
            return [1]
        temp = [str(i) for i in digits]
        number = int("".join(temp))

        return [int(i) for i in list(str(number + 1))]
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None or len(digits) == 0:
            return [1]
        move_one = 0
        digits[-1] += 1
        for i in reversed(range(len(digits))):
            if move_one + digits[i] >= 10:
                digits[i] = digits[i] + move_one - 10
                move_one = 1
            else:
                digits[i] += move_one
                move_one = 0

        if move_one == 1:
            list.insert(digits, 0, 1)

        return digits


if __name__ == '__main__':
    solution = Solution()
    l1 = [1,2,3]
    l2 = [4,3,2,1]
    l3 = []
    l4 = [9, 9]
    print(solution.plusOne(l1),solution.plusOne(l2),solution.plusOne(l3), solution.plusOne(l4))