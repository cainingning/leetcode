class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        """击败98%的用户"""
        map_dict = {1000: 'M', 900: 'CM', 500: 'D',400: 'CD',100: 'C',90:
            'XC',50: 'L',40: 'XL',10: 'X',9: 'IX',5: 'V', 4: 'IV',1: 'I', }
        result = ''
        for k, v in map_dict.items():
            while num >= k:
                times = num // k
                result += times * v
                num = num - times * k

        return result

so = Solution()
print(so.intToRoman(58))