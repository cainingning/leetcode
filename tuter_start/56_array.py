# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in range(len(intervals)):
            if res[-1].end < intervals[i].start:
                res.append(intervals[i])
            elif res[-1].end >= intervals[i].start and res[-1].end < intervals[i].end:
                res[-1].end = intervals[i].end
            elif res[-1].end >= intervals[i].end:
                continue

        return res

solution = Solution()
res = solution.merge([Interval(1,4),Interval(0, 4)])
for i in res:
    print(i.start, i.end)
