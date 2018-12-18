class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 0:
            return
        num = str(num)
        while len(num) >= 2:
            tmp = 0
            for i in range(len(num)-1, -1, -1):
                tmp += int(num[i])
            num = str(tmp)


        return int(num)

        ### another math method
        # return num-9*((num-1)//9)

if __name__ == '__main__':
    solution = Solution()
    print(solution.addDigits(38))