class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        a_len = len(a)
        b_len = len(b)
        if b_len > a_len:
            a, b = b, a
            a_len, b_len = b_len, a_len
        i, j, add_one = a_len - 1, b_len - 1, 0
        result = []
        while j >= 0:
            now_sum = int(a[i]) + int(b[j]) + add_one
            # print(i, j, a[i], b[j], add_one, now_sum)
            if now_sum >= 2:
                result.insert(0, now_sum - 2)
                add_one = 1
            else:
                result.insert(0, now_sum)
                add_one = 0
            j -= 1
            i -= 1
        while i >= 0:
            now_sum = int(a[i]) + add_one
            if now_sum >= 2:
                result.insert(0, now_sum - 2)
                add_one = 1
            else:
                result.insert(0, now_sum)
                add_one = 0
            i -= 1
        if add_one == 1:
            result.insert(0, 1)

        return "".join(str(x) for x in result)



if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("100", "110010"))
    i = [10]

