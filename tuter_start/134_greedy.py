class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0 or len(gas) != len(cost):
            return -1
        res = -1
        for i in range(len(gas)):
            remain = gas[i] - cost[i]
            if remain < 0:
                continue
            for j in range(i+1, len(gas)):
                remain = remain + gas[j] - cost[j]
                if remain < 0:
                    break
            if remain >= 0:
                for j in range(0, i):
                    remain = remain + gas[j] - cost[j]
                    if remain < 0:
                        break
            if remain >= 0:
                return i

        return res

    def canCompleteCircuit_2(self, gas, cost):
        """"""
        """如果油量的和大于等于花费的和，肯定是有解的。只需要找到剩余油量最小的位置，
        从他的下一个位置开始就可以得到最优解。"""
        import sys
        if sum(gas) < sum(cost):
            return -1
        start, total = 0, 0
        mm = sys.maxsize
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < mm:
                mm = total
                start = (i + 1) % len(gas)

        return start


solution = Solution()
print(solution.canCompleteCircuit_2(gas  = [1,2,3,4,5], cost = [3,4,5,1,2]))