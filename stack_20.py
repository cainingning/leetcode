class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        temp_stack = []
        left_symbol = ['[', '{', '(']
        right_symbol = [']', '}', ')']
        map_dict = {']':'[', '}':'{', ')':'('}
        for item in s:
            if item in left_symbol:
                temp_stack.append(item)
            elif item in right_symbol:
                if map_dict.get(item, 0) != 0 and len(temp_stack) >0 and map_dict.get(item) == temp_stack[-1]:
                    temp_stack.pop(-1)
                else:
                    return False
        if len(temp_stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("]"))