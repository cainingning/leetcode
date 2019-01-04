class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """罗马数字转整数
        击败了1%的解法。。。太差了"""
        map_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000,
                    'IV': 4, 'IX': 9, 'XL':40, 'XC': 90, 'CD': 400, 'CM': 900}
        num = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and map_dict.get(s[i:i+2], None):
                num += map_dict[s[i:i+2]]
                i += 2
            elif map_dict.get(s[i], None):
                num += map_dict[s[i]]
                i += 1

        return num

    def romanToInt_2(self, s):
        """

        :param s:
        :return:
        """
        """击败71%的人"""
        Int_num = 0
        for char in s:
            if char == 'I':
                Int_num = Int_num + 1

            if char == 'V':
                Int_num = Int_num + 5

            if char == 'X':
                Int_num = Int_num + 10

            if char == 'L':
                Int_num = Int_num + 50

            if char == 'C':
                Int_num = Int_num + 100

            if char == 'D':
                Int_num = Int_num + 500

            if char == 'M':
                Int_num = Int_num + 1000
        if 'IV' in s:
            Int_num = Int_num + (4 - 6) * s.count('IV')

        if 'IX' in s:
            Int_num = Int_num + (9 - 11) * s.count('IX')

        if 'XL' in s:
            Int_num = Int_num + (40 - 60) * s.count('XL')

        if 'XC' in s:
            Int_num = Int_num + (90 - 110) * s.count('XC')

        if 'CD' in s:
            Int_num = Int_num + (400 - 600) * s.count('CD')

        if 'CM' in s:
            Int_num = Int_num + (900 - 1100) * s.count('CM')

        return Int_num

