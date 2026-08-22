class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        start, end = newInterval
        i = 0
        n = len(intervals)

        # 1. Add intervals that are completely before newInterval
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        result.append([start, end])

        # 3. Add intervals that are completely after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result