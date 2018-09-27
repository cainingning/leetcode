class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        result = []
        self.generate_core(result, '', n, n)

        return result


    def generate_core(self, result, temp, l_num, r_num):
        # assert type(temp) == list
        if l_num == 0 and r_num == 0:
            result.append(temp)
            return
        if l_num == 0 and r_num > 0:
            self.generate_core(result, temp + ')', l_num, r_num - 1)
        elif l_num <= r_num:
            self.generate_core(result, temp + '(', l_num - 1, r_num)
            self.generate_core(result, temp + ')', l_num, r_num - 1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))