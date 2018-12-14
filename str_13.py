class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        b_map = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        result = 0
        i = 1
        while i <= len(s):
            # print(s[i])
            if s[i-1:min(i+1, len(s))] in b_map:
                result += b_map.get(s[i-1:i+1])
                i += 1
            else:
                result += a_map.get(s[i-1])
                # if i == len(s) - 1:
                #     result += a_map.get(s[-1])
            i += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("III"))

