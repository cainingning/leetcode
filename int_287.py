class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """这就是带环链表，找到环的入口就行。设置快慢节点
        设置速度为2倍的快慢指针，他们必定会在直线距离a=xo处相遇，a是出发点到环形入口o，x是相遇点。        
        """
        if len(nums) == 0:
            return 0
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        p_1 = nums[0]
        p_2 = slow
        while p_1 != p_2:
            p_1 = nums[p_1]
            p_2 = nums[p_2]

        return p_1



if __name__ == '__main__':
    solution = Solution()
    print(solution.findDuplicate( [1,3,4,2,2]))