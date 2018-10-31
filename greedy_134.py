class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) <= 0 or len(cost) <= 0 or len(gas) != len(cost):
            return -1
        gas_l = len(gas)
        remain_gas = []
        for i in range(gas_l):
            remain_gas.append(gas[i] - cost[i])
        for i in range(gas_l):
            cap = 0
            j = i
            ok_flag = True
            while True:
                cap += remain_gas[j]
                if cap < 0:
                    ok_flag = False
                    break
                j += 1
                if j == gas_l:
                    j = 0
            if ok_flag:
                return i
            if i == j:
                break

        return -1

    def canCompleteCircuit_2(self, gas, cost):
        """

        :param gas:
        :param cost:
        :return:
        """
        """
        定义diff[i] = gas[i] - cost[i]是每个站点地剩余油量
        从i出发，恰好到了j, sum1 = diff[i]+diff[i+1]...+diff[j] < 0 说明从i->j-1是可以行走的。那下一次尝试就不用从i+1开始，
        可以直接从j-1进行测试，恰好到了k, sum2 = diff[j-1]..diff[k] < 0 说明j-1->k-1是可以走的，再下一段走到了len-1这个
        位置sum3 > 0. 此时还要判断len-1到k-1是不是可行呢。只要判断sum3 + sum2 + sum1 >= 0 成立就可行了。即totall > 0
        """
        if len(gas) <= 0 or len(cost) <= 0 or len(gas) != len(cost):
            return -1
        start = 0
        total = 0
        sum = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if sum >= 0:
                sum += gas[i] - cost[i]
            else:
                start = i
                sum = gas[i] - cost[i]

        return start if total >= 0 else -1

    def canCompleteCircuit_3(self, gas, cost):
        """

        :param gas:
        :param cost:
        :return:
        """
        """
        diff[i] = gas[i] - cost[i]
        求一个点，使得从这个点出发diff的累加值能够达到峰值，转化成动态规划求和最大连续子序列问题。
        如果最后序列长度是数组长度，就返回序列起始位置，否则就返回-1
        """
        if len(gas) <= 0 or len(cost) <= 0 or len(gas) != len(cost):
            return -1

        l_min, g_min, l_max, g_max = 0, 0, 0, 0
        s_min, s_max, g_s_max, g_s_min = -1, -1, -1, -1
        e_min = -1
        total = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff

            if l_max < 0:
                s_max = i
                l_max = diff
            else:
                l_max += diff

            if l_max > g_max:
                g_max = l_max
                g_s_max = s_max

            if l_min > 0:
                l_min = diff
            else:
                l_min += diff

            if l_min < g_min:
                g_min = l_min
                e_min = i

        if total < 0:
            return -1
        elif g_max > total - g_min:
            return g_s_max
        else:
            return (e_min + 1) % len(gas)










if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit_3(gas  = [1,2,3,4,5], cost = [3,4,5,1,2]))