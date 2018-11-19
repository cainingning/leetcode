class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ###结果一定是最多m+n位长度的###
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j]) + carry
                # take care of the order of the next two lines
                carry = (res[i + j + 1] + tmp) // 10
                res[i + j + 1] = (res[i + j + 1] + tmp) % 10
                # or simply: carry, res[i+j+1] = divmod((res[i+j+1] + tmp), 10)
            res[i] += carry
        res = "".join(map(str, res))

        return '0' if not res.lstrip("0") else res.lstrip("0")


    def multiply_single(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        a_index = len(num1) - 1
        b_index = len(num2) - 1
        pre_count = 0
        result = []
        while a_index >= 0 and b_index >= 0:
            now_num = (int(num1[a_index]) * int(num2[b_index])) + pre_count
            #print('debug',int(num1[a_index]) * int(num2[b_index]))
            if now_num >= 10:
                pre_count = now_num // 10
                #print("进位是", pre_count)
                now_num = now_num - pre_count * 10
                print('debug stage2', now_num)
            else:
                pre_count = 0
            result.insert(0, now_num)
            a_index -= 1
            b_index -= 1

        while a_index >= 0:
            now_num = num1[a_index] + pre_count
            if now_num >= 10:
                pre_count = now_num % 10
                now_num = now_num - pre_count * 10
            else:
                pre_count = 0
            result.insert(0, now_num)
            a_index -= 1
        while b_index >= 0:
            now_num = num2[b_index] + pre_count
            if now_num >= 10:
                pre_count = now_num % 10
                now_num = now_num - pre_count * 10
            else:
                pre_count = 0
            result.insert(0, now_num)
            a_index -= 1
        if pre_count > 0 :
            result.insert(0, pre_count)

        result = [str(x) for x in result]

        return "".join(result)

if __name__ == '__main__':
    solution = Solution()
    print(solution.multiply(num1 = "123", num2 = "456"))
