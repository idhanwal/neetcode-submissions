class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res = [intervals[0]]
        count = 0
        for start, end in intervals[1:]:
            if res[-1][1] > start:
                count += 1
                res[-1][1] = min(res[-1][1], end)
            else:
                res.append([start, end])
        
        return count


