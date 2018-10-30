class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        str_list = list(s)
        j = len(str_list) - 1
        print(str_list)

        while i < j:
            tmp = str_list[j]
            str_list[j] = str_list[i]
            str_list[i] = tmp
            i += 1
            j -= 1

        return "".join(str_list)
