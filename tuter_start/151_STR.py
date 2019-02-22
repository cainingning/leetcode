class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.strip().split(" ")

        return " ".join(l[::-1])

solution = Solution()
print(solution.reverseWords("the sky is blue"))