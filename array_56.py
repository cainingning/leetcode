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
        if len(intervals) == 0:
            return []
        sorted_intervals = sorted(intervals, key=lambda x:x.start)
        result = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            if result[-1].end >= sorted_intervals[i].start and result[-1].end <= sorted_intervals[i].end:
                result[-1].end = sorted_intervals[i].end
            elif result[-1].end >= sorted_intervals[i].end:
                continue
            else:
                result.append(sorted_intervals[i])


        return result
