class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a is None:
            return b
        if b is None:
            return a
        a_n = int(a, base=2)
        b_n = int(b, base=2)
        c = a_n + b_n

        return str(bin(c))[2:]

solution = Solution()
print(solution.addBinary(a = "11", b = "0"))