class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        """2 abc, 3 def , 4 ghi
        """
        # 递归
        result = []
        self.combine("", digits, 0, result)

        return result

    def combine(self, prefix, digits, offset, result):
        maps = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if len(digits) <= offset:
            result.append(prefix)
            return result
        letters = maps.get(digits[offset], "")
        print(letters)
        for letter in letters:
            self.combine(prefix + letter, digits, offset + 1, result)

    def letterCombination(self, digits):
        maps = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(maps.get(digits[0], ""))
        prev = self.letterCombination(digits[: -1])
        other = list(maps.get(digits[-1], ""))
        return [p + o for p in prev for o in other]


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombination("23"))
    # print(ord("a") - 2)