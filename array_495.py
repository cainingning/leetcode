class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) <= 0 or duration <= 0:
            return 0
        active_time = 0
        start_time = timeSeries[0]
        end_time = start_time + duration
        for i in range(1, len(timeSeries)):
            if end_time <= timeSeries[i]:
                active_time += end_time - start_time
                start_time = timeSeries[i]
                end_time = timeSeries[i] + duration
            elif end_time <= timeSeries[i] + duration:
                end_time = timeSeries[i] + duration

        active_time += end_time - start_time

        return active_time

if __name__ == '__main__':
    solution = Solution()
    print(solution.findPoisonedDuration([1, 2], 2))



