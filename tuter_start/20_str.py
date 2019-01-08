class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 0:
            return True
        m = {')': '(', '}': '{', ']': '['}
        left = ['}', ')', ']']
        t_stack = []
        for item in s:
            if item not in left:
                t_stack.append(item)
            else:
                if m.get(item) and len(t_stack) > 0 and t_stack[-1] == m.get(item):
                    t_stack.pop(-1)
                else:
                    return False

        return True if len(t_stack) == 0 else False

solution = Solution()
print(solution.isValid(']'))