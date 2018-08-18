class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x > (pow(2, 31) - 1) or x < (-1 * pow(2, 31)):
            return 0
        elif x < 0:
             y = -1 * int(self.reverse_str(str(x)[1:]))
        else:
            y = int(self.reverse_str(str(x)))
        if y > (pow(2, 31) - 1) or y < (-1 * pow(2, 31)):
            return 0
        else:
            return y
    def reverse_str(self, s):
        str_list = [char for char in s]
        l = 0
        r = len(str_list) - 1
        while l < r:
            str_list[l], str_list[r] = str_list[r], str_list[l]
            l += 1
            r -= 1
        # print(str_list)
        return "".join(str_list)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(1534236469))
    print(pow(2, 31) - 1)
    if int(1534236469) > pow(2, 31) - 1:
        print("invalid")